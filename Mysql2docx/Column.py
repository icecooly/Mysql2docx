#!/usr/bin/python
#-*-coding:utf-8-*-

class Column:
    name = ''
    type = ''
    allowNull=''
    defaultValue=''
    comment=''

    def __init__(self, name,type,allowNull,defaultValue,comment):
        self.name = name
        self.type=type
        self.allowNull=allowNull
        self.defaultValue=defaultValue
        self.comment = comment

    def __str__(self):
        return self.name + "\t" + self.type + "\t" + self.allowNull + "\t" + self.defaultValue+"\t"+self.comment