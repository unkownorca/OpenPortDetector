from socket import *

# Function to check if a port is open
def cScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.settimeout(1)  # Set a timeout for the connection
        connskt.connect((tgtHost, tgtPort))
        print('[+] %d /tcp open' % tgtPort)
        connskt.close()
    except:
        print('[-] %d /tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Unable to resolve %s' % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n [+] Scan result for: %s ' % tgtName[0])
    except:
        print('\n [+] Scan result for: %s' % tgtIP)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('Scanning Port: %d' % tgtPort)
        cScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    portScan('google.com', [80, 22])
