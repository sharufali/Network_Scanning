# Title: Nmap Network Scanner CLI Tool
#
# Description:
# This Python script allows a user to perform various types of network scans
# on a specified target IP address using the Nmap tool. The user can choose
# between different scanning options such as:
#   1. Normal Network Scan
#   2. Software Version Detection
#   3. Full Port Scan
#   4. Operating System Detection
#
# The script uses the subprocess module to execute Nmap commands based on
# user input. It can be used for basic reconnaissance and network analysis
# tasks within a controlled or lab environment.
#
# Note: Nmap must be installed on the system for this script to work.


import subprocess

target_ip = "192.168.91.129"

print("Choose a scan option:")
print("1. Normal network scan")
print("2. Software Version Scan")
print("3. Port Scan")
print("4. OS Scan")

try:
    user_input = int(input("Enter your choice (1-4): "))
    if user_input == 1:
        subprocess.run(["nmap", target_ip])
    elif user_input == 2:
        subprocess.run(["nmap", target_ip, "-sV"])
    elif user_input == 3:
        subprocess.run(["nmap", target_ip, "-p-"])
    elif user_input == 4:
        subprocess.run(["nmap", target_ip, "-O"])
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
except ValueError:
    print("Please enter a valid number.")
