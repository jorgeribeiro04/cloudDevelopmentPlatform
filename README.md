#This project contains the instructions to automate the creation of a Virtual Machine on Google Cloud. The Virtual Machine has the following specifications:<br>
   Image: Ubuntu 20.04,<br>
   Disk Size: 250GB,<br>
   CPUs: 2,<br>
   RAM: 8GB<br>

#Step-by-step instructions for running the script:
   Create an account on Google Cloud.<br>
   Download and install Google CLI.<br>
   Access Google Cloud Console on the browser and create a new project. <br>
   Enable IAM and Compute Engine in your project.<br>
   Open the script on Visual Studio Code (or another IDE).<br>
   On your IDE’s terminal, run the commands “gcloud init” and “gcloud auth login”.<br>
   Run the following command to install the necessary libraries “python3 install google-auth google-api-python-client” (you may have to replace python3 with py or pip).<br>
   After installing the libraries, run the command “python3 script.py”.<br>
   Once the script is done, go back to Google Cloud Console, navigate to Compute Engine and then to VM instances to see the newly created virtual machine.<br>
   When the VM’s creation process is finished, click on SSH and run the following commands to install the Apache Server and configure the webpage:<br>
      sudo apt-get update<br>
      sudo apt-get install apache2 php7.0<br>
      echo ‘<!doctype html><html><body><h1>Hello World!</h1></body></html>’ | sudo tee /var/www/html/index.html<br>
   To access the website, click on the external IP address.<br>

#Prerequisites:<br>
   Google Cloud Account<br>
   Google Cloud CLI<br>
   IAM and Compute Engine enabled in your project.<br>

#Expected Output:<br>
If the script runs successfully, a “Setup Complete!” message will be displayed. Additionally, a virtual machine type 20.04 with 2 CPUs, 8GB of RAM and a disk size of 250 GB will created.
Troubleshooting 
If the script does not run in the first attempt, check if IAM and Compute Engine are enabled on your Google Cloud project. Additionally, ensure that you have all the necessary libraries installed. Lastly, set the variable “PROJECT” to the name of your project in the Google Cloud.
If the script runs in the first attempt, but fail in the next ones, make sure to change the “INSTANCE_NAME” and “STATIC_IP_NAME” variables, as they cannot be used more than once with the same value.



