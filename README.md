# LazySSLCheck
A tool to quickly identify which insecure TLS versions are in use, as well as insecure or weak ciphers. If there are no TLS versions or weak ciphers reported in the output then they are fine!

Requires:
- sslscan
- Python3
  
 Python3 Required Modules:
- requests
- os
- re
- argparse
- colorama
 
Usage:

> $ python3 lazysslcheck.py [IP ADDRESS] [PORT]
