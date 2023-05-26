#!/usr/bin/python
#-*-coding:utf-8-*-

class Column:
    name = ''
    type = ''
    allowNull=''
    defaultValue=''
    comment=''
    primaryKey=''

    def __init__(self, name,type,allowNull,defaultValue,comment,primaryKey):
        self.name = name
        self.type=type
        self.allowNull=allowNull
        self.defaultValue=defaultValue
        self.comment = comment
        self.primaryKey = primaryKey

    def __str__(self):
        return self.name + "\t" + self.type + "\t" + self.allowNull + "\t" + self.defaultValue+"\t"+self.comment