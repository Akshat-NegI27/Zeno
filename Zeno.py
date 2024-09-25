import requests
from bs4 import BeautifulSoup
import os
import sys
import re
import random
from colorama import Fore
w = Fore.WHITE
y = Fore.YELLOW
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
color = [w, y, r, g, b]
vegita = random.choice(color)
os.system('clear')
banner='''
███████╗███████╗███╗  ██╗ █████╗
╚════██║██╔════╝████╗ ██║██╔══██╗
  ███╔═╝█████╗  ██╔██╗██║██║  ██║
██╔══╝  ██╔══╝  ██║╚████║██║  ██║
███████╗███████╗██║ ╚███║╚█████╔╝
╚══════╝╚══════╝╚═╝  ╚══╝ ╚════╝

        [+] Which tool do you want to run ?

        [1]Dorker
        [2]Exploit
        [3]GDork Updater
        [4]Fuzzer

'''
print(vegita + banner + vegita)
tool = str(input(w + '    [-] Choose tool : ' + w))

if tool == "1":
    w = Fore.WHITE
    y = Fore.YELLOW
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    color = [w, y, r, g, b]
    vegita = random.choice(color)
    os.system('clear')
    banner1 = '''
    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗    
    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗   
    ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██████╔╝   
    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗   
    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗██║  ██║   
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   
                  
        [+] You Have List Of Sites ?
        
        [1] Yes        
        [2] No                                                                                 
    '''
    print(vegita + banner1 + vegita)
    
    site = str(input(w + '    [-] Choose : ' + w))
    if site == '1':
        list = input(w + '    [+] Enter the path for the site list: ' + w)
        if os.path.exists(list) is False:
            print(w + '    [-] ' + w + r + 'Either file do not exist or path for file is invalid.' + r)
        else:
            print(w + '    [+] File found: ' + w + g + 'True' + g)
            file = open(list, 'r')
            read = file.readlines()
            x = len(read)
            x = str(x)
            print(w + '    [+] Total Domains: ' + w + g + x + g)
            dorks = '''
        [-] Choose The dork you want to search for: 
                    
        [1] Directory listing vulnerabilities         [10] Open Redirects                      [19] Search in WayBack Machine #2                           
        [2] Exposed Configuration files               [11] Find Pastebin entries               [X]  For Exit
        [3] Exposed Database files                    [12] Employees on LINKEDIN                  
        [4] Find WordPress                            [13] .htaccess sensitive files                                     
        [5] Exposed log files                         [14] Find Subdomains           
        [6] Backup and old files                      [15] Find Sub-Subdomains            
        [7] Publicly exposed documents                [16] Find WordPress [Wayback Machine]
        [8] phpinfo()                                 [17] Find .SWF file (Google)                     
        [9] Install / Setup files                     [18] Search SWF in WayBack Machine                                           
                                    
                                                     
            '''
            print(vegita + dorks + vegita)
            dork = input(w + '    [-] Choose : ' + w)
            for target in read:
                if dork == '1':
                    print(" ")
                    print(
                        w + '    [+] ' + w + vegita + 'Looking for Directory listing vulnerabilities in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+intitle:index.of'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '      [+] ' + w + r + 'Connection Error' + r)
                elif dork == '2':
                    print(" ")
                    print(
                        w + '    [+] ' + w + vegita + 'Looking for Exposed Configuration files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '3':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Exposed Database files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:sql+|+ext:dbf+|+ext:mdb'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '4':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Find WordPress in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+inurl:wp-+|+inurl:wp-content+|+inurl:plugins+|+inurl:uploads+|+inurl:themes+|+inurl:download'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '5':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Exposed log files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:log'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '6':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Backup and old files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                
                elif dork == '7':
                    print(" ")
                    print(
                        w + '    [+] ' + w + vegita + 'Looking for Publicly exposed documents in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '8':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for phpinfo() in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
               
                elif dork == '9':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Install / Setup files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '10':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Open Redirects in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                
                elif dork == '11':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Pastebin entries in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:pastebin.com+' + target
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '12':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for Employees on LINKEDIN in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:linkedin.com+employees+' + target
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '13':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for .htaccess sensitive files in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:' + target + '+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+simple.com%20-github'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '14':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Finding Subdomains ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:*.' + target
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '15':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Finding Sub-Subdomains ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=site:*.*.' + target
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                
                elif dork == '16':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for WordPress [Wayback Machine] ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'http://wwwb-dedup.us.archive.org:8083/cdx/search?url=' + target + '/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '17':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Looking for .SWF file (Google) in ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://www.google.com/search?q=+inurl:' + target + '+ext:swf'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        ok = soup.find_all('div', class_='kCrYT')
                        ok = str(ok)
                        new = re.findall('<a href="(.*?)"', ok)
                        new_link = len(new)
                        if new_link > 1:
                            for i in new:
                                i = str(i)
                                if i.startswith('/url?q=') is True:
                                    i = i[7:-100]
                                    print(w + '    [+] Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [+] ' + w + r + 'No Link found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == '18':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Searching SWF in WayBack Machine for ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'
                        response = requests.get(url)
                        response = response.text
                        length = len(response)
                        if length > 1:
                            response = response.splitlines()
                            for i in response:
                                print(w + '    [+]Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [-]' + w + r + ' No Link Found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '    [+] ' + w + r + 'Connection Error' + r)
                elif dork == '19':
                    print(" ")
                    print(w + '    [+] ' + w + vegita + 'Searching in WayBack Machine #2 for ' + vegita + r + target + r)
                    print(w + '    [+] Target: ' + w + vegita + target + vegita)
                    print(" ")
                    try:
                        url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000&_=1507209148310'
                        response = requests.get(url)
                        response = response.text
                        length = len(response)
                        if length > 1:
                            response = response.splitlines()
                            for i in response:
                                print(w + '    [+]Link Found: ' + w + g + i + g)
                        else:
                            print(w + '    [-]' + w + r + ' No Link Found' + r)
                    except requests.exceptions.ConnectionError as e:
                        print(w + '     [+] ' + w + r + 'Connection Error' + r)
                elif dork == 'X':
                    print(w + '     [-] ' + w + r + 'KK bye.Exiting.' + r)
                else:
                    print(w + "    [-] " + w + r + "I don't understand you!! Exiting" + r)
                    sys.exit()
    elif site == '2':
        target = input(w + '    [+] Enter the target domain: ' + w)
        dorks = '''
        [+] Choose The dork you want to search for: 
    
        [1] Directory listing vulnerabilities         [10] Open Redirects                      [19] Search in WayBack Machine #2                           
        [2] Exposed Configuration files               [11] Find Pastebin entries               [X]  For Exit
        [3] Exposed Database files                    [12] Employees on LINKEDIN                  
        [4] Find WordPress                            [13] .htaccess sensitive files                                     
        [5] Exposed log files                         [14] Find Subdomains           
        [6] Backup and old files                      [15] Find Sub-Subdomains            
        [7] Publicly exposed documents                [16] Find WordPress [Wayback Machine]
        [8] phpinfo()                                 [17] Find .SWF file (Google)                     
        [9] Install / Setup files                     [18] Search SWF in WayBack Machine                    
            '''
        print(vegita + dorks + vegita)
        dork = input(w + '    [+] Choose : ' + w)
        if dork == '1':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Directory listing vulnerabilities in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+intitle:index.of'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '      [+] ' + w + r + 'Connection Error' + r)
        elif dork == '2':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Exposed Configuration files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '3':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Exposed Database files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:sql+|+ext:dbf+|+ext:mdb'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '4':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Find WordPress in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+inurl:wp-+|+inurl:wp-content+|+inurl:plugins+|+inurl:uploads+|+inurl:themes+|+inurl:download'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '5':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Exposed log files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:log'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '6':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Backup and old files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        
        elif dork == '7':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Publicly exposed documents in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '8':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for phpinfo() in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        
        elif dork == '9':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Install / Setup files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '10':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Open Redirects in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '11':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Pastebin entries in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:pastebin.com+' + target
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '12':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for Employees on LINKEDIN in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:linkedin.com+employees+' + target
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '13':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for .htaccess sensitive files in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:' + target + '+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+simple.com%20-github'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '14':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Finding Subdomains ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:*.' + target
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '15':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Finding Sub-Subdomains ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=site:*.*.' + target
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        
        elif dork == '16':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for WordPress [Wayback Machine] ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'http://wwwb-dedup.us.archive.org:8083/cdx/search?url=' + target + '/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '17':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Looking for .SWF file (Google) in ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://www.google.com/search?q=+inurl:' + target + '+ext:swf'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                ok = soup.find_all('div', class_='kCrYT')
                ok = str(ok)
                new = re.findall('<a href="(.*?)"', ok)
                new_link = len(new)
                if new_link > 1:
                    for i in new:
                        i = str(i)
                        if i.startswith('/url?q=') is True:
                            i = i[7:-100]
                            print(w + '    [+] Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [+] ' + w + r + 'No Link found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == '18':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Searching SWF in WayBack Machine for ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'
                response = requests.get(url)
                response = response.text
                length = len(response)
                if length > 1:
                    response = response.splitlines()
                    for i in response:
                        print(w + '    [+]Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [-]' + w + r + ' No Link Found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '    [+] ' + w + r + 'Connection Error' + r)
        elif dork == '19':
            print(" ")
            print(w + '    [+] ' + w + vegita + 'Searching in WayBack Machine #2 for ' + vegita + r + target + r)
            print(w + '    [+] Target: ' + w + vegita + target + vegita)
            print(" ")
            try:
                url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000&_=1507209148310'
                response = requests.get(url)
                response = response.text
                length = len(response)
                if length > 1:
                    response = response.splitlines()
                    for i in response:
                        print(w + '    [+]Link Found: ' + w + g + i + g)
                else:
                    print(w + '    [-]' + w + r + ' No Link Found' + r)
            except requests.exceptions.ConnectionError as e:
                print(w + '     [+] ' + w + r + 'Connection Error' + r)
        elif dork == 'X':
            print(w + '     [-] ' + w + r + 'KK bye.Exiting.' + r)
        else:
            print(w + "    [-] " + w + r + "I don't understand you!! Exiting" + r)
            sys.exit()
    else:
        print(r + "    [-] I don't understand you!! Exiting" + r)
        sys.exit()
    
        
#++++++++++++++++++++++++++++++++++++++++++++ Exploit ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

elif tool == '2':
    w = Fore.WHITE
    y = Fore.YELLOW
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    color = [w, y, r, g, b]
    vegita = random.choice(color)
    os.system('clear')
    banner2 = """
    
    ███████╗██╗  ██╗██████╗ ██╗      █████╗ ██╗████████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔══██╗██║╚══██╔══╝
    █████╗   ╚███╔╝ ██████╔╝██║     ██║  ██║██║   ██║
    ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║  ██║██║   ██║
    ███████╗██╔╝╚██╗██║     ███████╗╚█████╔╝██║   ██║
    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚════╝ ╚═╝   ╚═╝            
    """ 
    def bnPrint():
        print(vegita + banner2 + vegita)
        print('\n')
    bnPrint()
    #-----------------------------------------------------------------------------#
        
    titles = []
    urls= []
        
    print(' ')
    print(w + '     [+] -------------------------- ' + w + vegita + ' Latest Exploits and CVEs' + vegita + w + ' -------------------------- [+] ')
    print(' ')
        
    url = 'https://cxsecurity.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i in soup.find_all('div', class_='col-md-8'):
        links = i.find('a')
        link = links.get('href')
        urls.append(link)
    for i in soup.findAll('div', class_='col-md-8'):
        title = i.text
        titles.append(title)
    x = 0
    for i in titles:
        print(w + '     [' + w + g + str(x) + g + w + '] ' + vegita + i + vegita)
        x += 1
    
    print(' ')
    choice = int(input(w + '     [+] ' + w + vegita + 'Enter a number to continue with: '))
    
    def read(num):
        _response = requests.get(urls[num])
        _soup = BeautifulSoup(_response.content, 'html.parser')
        _body = _soup.find('div', class_='well well-sm premex')
        print(w + '     [+] -------------------------- ' + w + vegita + titles[num] + vegita + w + ' -------------------------- [+] ')
        print(' ')
        print(vegita + _body.text + vegita)
    
    read(choice)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++ GDork Updater ++++++++++++++++++++++++++++++++++++++++++++
elif tool == '3':
    w = Fore.WHITE
    y = Fore.YELLOW
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    color = [w, y, r, g, b]
    vegita = random.choice(color)
    os.system('clear')

    banner3 = """
     ██████╗ ██████╗  ██████╗ ██████╗ ██╗  ██╗     ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
    ██╔════╝ ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    ██║  ███╗██║  ██║██║   ██║██████╔╝█████╔╝█████╗██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
    ██║   ██║██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
    ╚██████╔╝██████╔╝╚██████╔╝██║  ██║██║  ██╗     ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    
    """
    print(vegita + banner3 + vegita)
    print('\n')
    links = []
    titles = []
    dorks = []
    url = 'https://cxsecurity.com/dorks/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i in soup.findAll('a'):
        link = i.get('href')
        if link.startswith('https://cxsecurity.com/issue/') is True:
            title = i.get('title')
            titles.append(title)
            links.append(link)
        else:
            pass
    for i in soup.findAll('font', color="#FCFCFC"):
        dork = i.text
        dorks.append(dork)
    x = 0
    while x <= 19:
        print(w + '     [' + vegita + str(x) + w + '] ' + vegita + 'Title: ' + g + titles[x])
        print(w + '     [' + vegita + '+' + w + ']  ' + g + dorks[x])
        print('\n')
        x +=1
    num = int(input(w +'     [' + vegita + '+' + w + '] ' + vegita + 'Enter a number to continue: '))
    def exploit(number):
        _response = requests.get(links[number])
        _soup = BeautifulSoup(_response.content, 'html.parser')
        read = _soup.find('div', class_="well well-sm premex")
        print('\n')
        print(w + '[+]' + vegita + '----------------- ' + g + titles[number] + vegita + ' ---------------------' + w + '[+]')
        print('\n')
        print(g + read.text)
    exploit(num)
    new_dork = dorks[num]
    goku = new_dork.replace('Dork:', ' ')
    useragents = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
              'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
          'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
          'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
          'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
          'Microsoft Internet Explorer/4.0b1 (Windows 95)',
          'Opera/8.00 (Windows NT 5.1; U; en)',
          'amaya/9.51 libwww/5.4.0',
          'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
          'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
          'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
          'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
          'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
          'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
    headers = {'user-agent': random.choice(useragents)}
    new_url = 'https://www.google.com/search?q='+goku
    new_response = requests.get(url=new_url, headers=headers)
    new_soup = BeautifulSoup(new_response.content, 'html.parser')
    print('\n')
    print(w + '[+]' + vegita + '-------------------' + g + 'Vulnerable urls' + vegita + '---------------------------' + w + '[+]')
    print('\n')
    for i in new_soup('a'):
        hf = i.get('href')
        if hf.startswith('/url?q=') is True:
            new_link = hf[7:-88]
            if (new_link.startswith('https://support.google.com') or new_link.startswith('https://accounts.google.com')) is False:
                vuln_link = new_link.replace('%3D', '=')
                final_link = vuln_link.replace('%3F','?')
                print(w + '     [' + vegita + '+' + w + '] ' + g + final_link)
            else:
                pass
        else:
            pass  

#++++++++++++++++++++++++++++++++++++++++ Fuzzer +++++++++++++++++++++++++++++++++++++++++++++++++++

elif tool == '4':
    w = Fore.WHITE
    y = Fore.YELLOW
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    color = [w, y, r, g, b]
    vegita = random.choice(color)
    os.system('clear')
    banner4 = """
     
    ███████╗██╗   ██╗███████╗███████╗███████╗██████╗
    ██╔════╝██║   ██║╚════██║╚════██║██╔════╝██╔══██╗
    █████╗  ██║   ██║  ███╔═╝  ███╔═╝█████╗  ██████╔╝
    ██╔══╝  ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ 
    
    """
    print(vegita + banner4 + vegita)
    print('\n')
    target = input(w + '   [+] Enter The Target like=[http://Example.com/]= ' + w)
    print("using default wordlist")
    op =open('list.txt', 'r')
    paths = op.readlines()
    for path in paths:
        url = target + path
        try:
            status = requests.get(url).status_code
            if status == 200:
                print(vegita + url + "[200]")
            elif status == 403 or status == 404:
                print(r + url + str(status))
            else:
                pass
        except:
            print(r + "Check the target url! or your internet connection")
