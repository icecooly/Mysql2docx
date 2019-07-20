#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os
from os import path

"""
See https://github.com/icecooly/Mysql2docx
"""

VERSION = '1.6'

DESCRIPTION = (
    '自动生成数据库设计文档'
)

setup(
        name='Mysql2docx', 
        version=VERSION, 
        description="mysql自动生成数据库设计文档",
        long_description=DESCRIPTION,
        classifiers=[],
        keywords='自动数据库设计文档',
        include_package_data = True,
        author='skydu',
        author_email='icecooly.du@qq.com', 
        url='https://github.com/icecooly/Mysql2docx',
        license='MIT',
        packages=find_packages(),
        install_requires=['python-docx','pymysql'],
        extras_require={}
)
