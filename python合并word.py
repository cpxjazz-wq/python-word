# -*- coding: utf-8 -*-

import win32com.client as win32
import os
word = win32.gencache.EnsureDispatch('Word.Application')
#启动word对象应用
word.Visible = False
path = r'E:\hb doc'
files = []
for filename in os.listdir(path):
    filename = os.path.join(path,filename)
    files.append(filename)
#新建合并后的文档
output = word.Documents.Add()
for file in files:
    output.Application.Selection.InsertFile(file)#拼接文档
#获取合并后文档的内容
doc = output.Range(output.Content.Start, output.Content.End)
output.SaveAs('E://hb doc//result.docx') #保存
output.Close()