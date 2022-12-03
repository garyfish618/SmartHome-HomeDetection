import nmap
from database_client import db

def start_scanning():
    registered_host = ''

    while True:
        nm = nmap.PortScanner()
        nm.scan("192.168.50.0/24", arguments=("-sn"))
        scanned_hosts = nm.all_hosts()
        connected_hosts = []

        for host in db['hosts_to_watch'].find({}):
            if host in scanned_hosts and host not in connected_hosts:
                connected_hosts.append(host)
                print("Host ", host, " joined")
            
            elif host not in scanned_hosts and host in connected_hosts:
                connected_hosts.remove(host)
                print("Host ", host, " has disconnected")


            
    
