#!/usr/bin/python
#-*-coding:utf-8-*-

class Table:
    name = ''
    comment = ''
    columns=[]

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

    def __str__(self):
        return self.name + "\t" + self.comment
