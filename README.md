# Mysql2docx
自动生成数据库设计文档

## 安装
[需要python3.0以上]
 
```shell
pip3 install Mysql2docx
```


## 使用
```python
>>> from Mysql2docx import Mysql2docx
>>> Mysql2docx.do('127.0.0.1','root','password','db_test',3306)
```
如果参数正确会成功生成>>数据库设计文档.docx

## 截图
![](https://github.com/icecooly/Mysql2docx/blob/master/example.jpg)
