# Mysql2docx
自动生成数据库设计文档

## 安装
[需要python3.0以上]
 
```shell
pip install Mysql2docx
```


## 使用
```python
>>> from Mysql2docx import Mysql2docx
>>> m=Mysql2docx()
>>> m.do('127.0.0.1','root','password','db_test',3306)
```
如果参数正确会成功生成>>数据库设计文档.docx

## 截图
![](https://gitee.com/icecooly/Mysql2docx/attach_files/download?i=92257&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F01%2FC2%2FPaAvDFmfDX2AbSPhAAH-JDNEN-o933.png%3Ftoken%3D314a024565ec3e8df4ec6964413aacba%26ts%3D1503595901%26attname%3Dlizi.png)
