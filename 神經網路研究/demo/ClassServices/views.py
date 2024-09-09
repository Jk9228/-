from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import mysql.connector
from django.http import JsonResponse
import json

# Create your views here.
class connect_mysql_info:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost', 
            port='3306',
            user='Jk9228', 
            password='1234'
            )

        self.cursor = self.connection.cursor()

        self.cursor.execute("use ooschool;")
        
    def member_info_all(self):

        self.cursor.execute("SELECT * FROM member ORDER BY age DESC limit 3;")

        records = self.cursor.fetchall()

        return records
    
    def member_info_name(self):

        self.cursor.execute("SELECT name FROM member ORDER BY age DESC limit 3;")

        records = self.cursor.fetchall()

        return records
    
    def member_info_age(self):
        
        self.cursor.execute("SELECT age FROM member ORDER BY age DESC limit 3;")

        records = self.cursor.fetchall()

        return records
    
    def member_info_add(self, name, id, interest):
        try:    
            self.cursor.execute("INSERT INTO student VALUES(%s, %s, %s)",(name ,id, interest))
            self.cursor.commit()
            return HttpResponse("insert complete")
        except mysql.connector.Error:
            self.connection.rollback()
            return HttpResponse("insert fail")
        
        
    def check_change(self):
        return self.cursor.rowcount
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    
def reverse_string(string):
    return string[::-1] # 聽說python的切片語法很強大，目前用來顛倒字串

def starify(string):
    vowels = 'aeiouAEIOU' #定義母音
    result = [] #儲存結果
    
    for char in string: #跑字串裡的每個字母
        if char in vowels: #如果字母為母音
            result += "*" #就換成*
        else :
            result += char #如果不是就直接儲存原字母
            
    return result

def studentMethod(request):
    connection = connect_mysql_info()
    
    if request.method == 'POST':
        reg = request.body.decode('UTF-8')
        
        print(type(reg))  # 列印解碼後的類型
        reg = json.loads(reg)
        
        print(type(reg), reg)  # 列印JSON轉換後的類型和內容
        
        method = reg.get('Method')
        
        if method == "upload":
            name = reg.get('Name', 'Stranger')# 獲取'Name'參數，默認為'Stranger'
            id = reg.get('ID', 'z00000000')
            interest = reg.get('Interest')
            connection.member_info_add(name, id, interest)
                
        elif method == "reverse":
            string = "hello"
            return HttpResponse(reverse_string(string))
        
        elif method == "upper":
            string = "hello"
            return HttpResponse(string.upper())
            
        elif method == "starify":
            string = "hello"
            return HttpResponse(starify(string))
        
        connection.close_connection()
        return HttpResponse(f"Hello, {name}")
    
    # 如果請求不是POST，返回方法名稱
    connection.close_connection()
    
    reg = request.method
    return JsonResponse({'foo': reg})