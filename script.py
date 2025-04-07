import time
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


PROJECT = "cloudplatformdevelopment2"
REGION = "europe-west2"
ZONE = "europe-west2-a"
INSTANCE_NAME = "jorge-ribeiro-vm"
STATIC_IP_NAME = "jorge-net"
IMAGE = "ubuntu-os-cloud"
IMAGE_NAME = "ubuntu-2204-jammy-v20230428"

CUSTOM_CPU = 2
CUSTOM_MEMORY_MB = 8192
DISK_SIZE_GB = 250


def create_static_ip(compute):
    body = {"name": STATIC_IP_NAME}
    try:
        compute.addresses().insert(project=PROJECT, region=REGION, body=body).execute()
    except HttpError as err:
        if err.resp.status == 409:
            print("Static IP already exists.")
        else:
            raise
    time.sleep(2)
    response = compute.addresses().get(project=PROJECT, region=REGION, address=STATIC_IP_NAME).execute()
    return response.get("address")


def get_image_link(compute):
    image = compute.images().get(project=IMAGE, image=IMAGE_NAME).execute()
    return image["selfLink"]


def ensure_firewall_rule(compute):
    rule = {
        "name": "allow-http-ssh-traffic-jorgeribeirovm",
        "network": "global/networks/default",
        "allowed": [{"IPProtocol": "tcp", "ports": ["80", "22"]}],
        "sourceRanges": ["0.0.0.0/0"],
        "targetTags": ["http-server"]
    }
    try:
        compute.firewalls().insert(project=PROJECT, body=rule).execute()
    except HttpError as err:
        if err.resp.status == 409:
            print("Firewall rule already exists.")
        else:
            raise


def create_instance(compute, external_ip, image_link):
    machine_type_path = f"zones/{ZONE}/machineTypes/custom-{CUSTOM_CPU}-{CUSTOM_MEMORY_MB}"
    config = {
        "name": INSTANCE_NAME,
        "machineType": machine_type_path,
        "disks": [{
            "boot": True,
            "autoDelete": True,
            "initializeParams": {
                "diskSizeGb": DISK_SIZE_GB,
                "sourceImage": image_link
            }
        }],
        "networkInterfaces": [{
            "network": "global/networks/default",
            "accessConfigs": [{
                "name": "External NAT",
                "type": "ONE_TO_ONE_NAT",
                "natIP": external_ip
            }]
        }],
        "tags": {"items": ["http-server"]}
    }

    compute.instances().insert(project=PROJECT, zone=ZONE, body=config).execute()


def main():
    creds, _ = google.auth.default()
    compute = build("compute", "v1", credentials=creds)

    ip_address = create_static_ip(compute)
    if not ip_address:
        print("Unable to acquire static IP.")
        return

    image_link = get_image_link(compute)
    ensure_firewall_rule(compute)
    create_instance(compute, ip_address, image_link)

    print("Setup complete!")


if __name__ == "__main__":
    main()
