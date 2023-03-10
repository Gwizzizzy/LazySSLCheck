import requests
import os
import re
import argparse

p = argparse.ArgumentParser(description="A tool to quickly identify which insecure TLS versions are in use, as well as insecure or weak ciphers. If there are no TLS versions or weak ciphers reported in the output then they are fine! Oooweeee!")
p.add_argument("host",help = "Hostname or IP address")
p.add_argument("port", type=str , help= "Port number i.e. 443")
args = p.parse_args()
host = args.host
port = args.port

tls1_0 = "1.0.\senabled..1" 
tls1_1 = "1.1.\senabled..1"
cipherSearch = "cipher=.(.*?)..id"


os.system('sslscan --xml=sslscanout ' + host + ':' + port) #runs sslscan

sslScanOutput = open("sslscanout","r")

sslScanContent = sslScanOutput.read() # reads the content of sslScanOutput

"""
def sslScanMode():
    if 
"""

def ciphercheck():

    outfile=open('results.txt','w')
    if re.search(tls1_0,str(sslScanContent)): # if TLSv1.0 or TLSv1.1 is enabled print the following messages.
        print('\n'+"TLSv1.0 Enabled!")
        outfile.write("TLSv1.0 Enabled!"+'\n')


    if re.search(tls1_1,str(sslScanContent)):
        print("TLSv1.1 Enabled!"+'\n')
        outfile.write("TLSv1.1 Enabled!"+'\n')


    ciphers = re.findall(cipherSearch,str(sslScanContent)) # finds all the ciphers in the sslscan output
    
    for c in ciphers: # for every cipher found in sslScanScontent
    
        response = requests.get('https://ciphersuite.info/search/?q='+c) # run a query on ciphersuite.info
        weak = (".Weak..span.")
        insecure = (".Insecure..span.")
        if re.search(weak,str(response.content)): # if the response contains Weak</span> print the cipher and is weak
            print("Weak cipher identified: "+c)
            outfile.write("Weak cipher identified: "+c+'\n')
        
        elif re.search(insecure,str(response.content)): # if the response contains Insecure</span> print the cipher and is insecure
            print("Insecure cipher identified: "+c)
            outfile.write("Insecure cipher identified: "+c+'\n')
        
""" Outputs None to a file :(
outfile=open('results.txt','w')
outfile.write(str(ciphercheck()))
"""
ciphercheck()    









