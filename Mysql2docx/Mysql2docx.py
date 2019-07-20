#!/usr/bin/python
#-*-coding:utf-8-*-

import json
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import pymysql
from . import Table
from . import Column

__author__ = 'skydu'

class Mysql2docx(object):
    dbName = ''
    #
    def __init__(self):
        dbName = ''

    def getComment(self,comment):
        if comment==None:
            return ""
        try:
            data=json.loads(comment)
            return data[0]['value']
        except:
            return comment

    def getTables(self,db):
        sql = "select table_name, TABLE_COMMENT from information_schema.tables " \
              "where table_schema = '%s' and table_type = 'base table'"%self.dbName
        cursor=db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        tables=list()
        for table in data:
            t=Table(table[0], self.getComment(table[1]));
            tables.append(t)
        cursor.close()
        return tables

    def getColumns(self,db,tableName):
        sql = "SELECT  " \
              "COLUMN_NAME 列名,  " \
              "COLUMN_TYPE 数据类型,  " \
              "IS_NULLABLE 是否为空,    " \
              "COLUMN_DEFAULT 默认值,    " \
              "COLUMN_COMMENT 备注   " \
              "FROM  INFORMATION_SCHEMA.COLUMNS  " \
              "where  table_schema ='%s'  AND   table_name  = '%s';" % (self.dbName, tableName)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        columns=list()
        for column in data:
            c=Column(column[0],column[1],column[2],column[3],self.getComment(column[4]))
            columns.append(c)
        cursor.close()
        return columns

    @staticmethod
    def do(dbHost, dbUser, dbPassword, dbName, dbPort,doc='数据库设计文档.docx'):
        print("dbHost:%s,dbUser:%s,dbPassword:%s,dbName:%s,dbPort:%d" % (dbHost, dbUser, dbPassword, dbName, dbPort))
        instance=Mysql2docx()
        instance.dbName=dbName
        db = pymysql.connect(dbHost, dbUser, dbPassword, dbName, dbPort, charset="utf8")
        tables = instance.getTables(db);
        for table in tables:
            tableName = table.name
            table.columns = instance.getColumns(db, tableName)

        document = Document()
        p = document.add_paragraph()
        paragraph_format = p.paragraph_format
        run = p.add_run('数据库设计文档')
        run.font.size = Pt(24)
        paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        for table in tables:
            print("table:%s" % table)
            document.add_heading("表%s[%s]" % (table.name, table.comment), 2)
            t = document.add_table(rows=len(table.columns) + 1, cols=5)
            cells = t.rows[0].cells
            cells[0].text = '字段名'
            cells[1].text = '字段类型'
            cells[2].text = '可以为空'
            cells[3].text = '默认值'
            cells[4].text = '注释'
            i = 0
            for column in table.columns:
                i += 1
                rowCells = t.rows[i].cells
                rowCells[0].text = column.name
                rowCells[1].text = column.type
                rowCells[2].text = column.allowNull
                if column.defaultValue!=None:
                    rowCells[3].text = column.defaultValue
                rowCells[4].text = column.comment
            #
            document.add_page_break()
        #
        document.save(doc)
