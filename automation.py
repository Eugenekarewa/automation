import subprocess
import re
import os
def run_command(command):
    """run a system command and returns the output"""
    result=subprocess.run(command,shell=True,capture_output=True,text=True)
    return result.stdout
def run_nmap(target):
    command =f"sudo nmap -sV -P- -SC {target} -oN scans.txt"
    print("running nmap scan ...patience is required ...well you can as well as give up ,who cares !")
    return run_command(command)
def extract_ports(output,service):
    pattern=re.compile(rf'(\d+/tcp)\s+{service}',re.IGNORECASE)
    return [match.group(1).split('/')[0]for match in pattern.finditer(output)]
def run_ffuf(target,ports):
    wordlist='/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt'
    results={}
    for port in ports:
        print(f"running ffuf on port {port} ...")
        command =f"ffuf -u http://{target}:{port}/FUZZ -w {wordlist} -o ffuf_results_{port}.txt"
        output=run_command(command)
        with open(f"ffuf_results_{port}.txt","w")as f:
             f.write(output)
        results[port]=output
    return results

def search_exploits(service,version):
    print(f"searching for exploits for {service}{version}...")
    command=f"searchsploit '{service}{version}'"
    return run_command(command)

def main(target):
    nmap_output=run_nmap(target)
    http_ports=extract_ports(nmap_output,'http')
    ssh_ports=extract_ports(nmap_output,'ssh')
    if http_ports:
       ffuf_results=run_ffuf(target,http_ports)
       for port, result in ffuf_results.items():
           print(f"ffuf results for port {port}:\n{result}")
    print("searching for exploits...")
    for line in nmap_output.splitlines():
        if '/tcp' in line:
           service_info=line.split()
           if len(service_info)>2:
              service=service_info[2]
              version=service_info[3] if len(service_info)>3 else ''
              exploits=search_exploits(service,version)
              print(f"exploits for {service}{version}:\n{exploits}")

     
if __name__=="__main__":
   target_ip=input("enter the target ip: ")
   main(target_ip)

