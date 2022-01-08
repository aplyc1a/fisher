# MyHttpsServer

Why those `potato` often use HFS to dispatch their toys?!

## 功能

1.在公网提供安全的https文件下发服务。服务器启动后会将data目录下的文件拷贝到html下的随机目录中。

2.记录GET/POST请求细节。log/access.log可以记录GET/POST的具体内容，方便携带敏感数据及POC测试。

## 特点


1.抗目录爆破。

2.抗流量分析。

3.支持Windows/Linux双平台运行。

## 部署

step1: 生成https证书。强烈建议自己手动生成一个，否则会存在一定特征。

```shell
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

step2: 将待下发文件放置在data目录中。

step3: 运行以下命令。


```shell
python3 MyHttpsServer.py -p 56221
```


