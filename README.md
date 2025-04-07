#This project contains the instructions to automate the creation of a Virtual Machine on Google Cloud. The Virtual Machine has the following specifications:
   Image: Ubuntu 20.04,
   Disk Size: 250GB,
   CPUs: 2,
   RAM: 8GB

#Step-by-step instructions for running the script:
  - Create an account on Google Cloud.
  - Download and install Google CLI.
  - Access Google Cloud Console on the browser and create a new project. 
  - Enable IAM and Compute Engine in your project.
  - Open the script on Visual Studio Code (or another IDE).
  - On your IDE’s terminal, run the commands “gcloud init” and “gcloud auth login”.
  - Run the following command to install the necessary libraries “python3 install google-auth google-api-python-client” (you may have to replace python3 with py or pip).
  - After installing the libraries, run the command “python3 script.py”.
  - Once the script is done, go back to Google Cloud Console, navigate to Compute Engine and then to VM instances to see the newly created virtual machine.
  - When the VM’s creation process is finished, click on SSH and run the following commands to install the Apache Server and configure the webpage:
      - sudo apt-get update
      - sudo apt-get install apache2 php7.0
      - echo ‘<!doctype html><html><body><h1>Hello World!</h1></body></html>’ | sudo tee /var/www/html/index.html
  - To access the website, click on the external IP address.

#Prerequisites:
  - Google Cloud Account
  - Google Cloud CLI
  - IAM and Compute Engine enabled in your project.

#Expected Output:
If the script runs successfully, a “Setup Complete!” message will be displayed. Additionally, a virtual machine type 20.04 with 2 CPUs, 8GB of RAM and a disk size of 250 GB will created.
Troubleshooting 
If the script does not run in the first attempt, check if IAM and Compute Engine are enabled on your Google Cloud project. Additionally, ensure that you have all the necessary libraries installed. Lastly, set the variable “PROJECT” to the name of your project in the Google Cloud.
If the script runs in the first attempt, but fail in the next ones, make sure to change the “INSTANCE_NAME” and “STATIC_IP_NAME” variables, as they cannot be used more than once with the same value.



