from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
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
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class member:
    def members_info(records):
        members_info = []
        members_info.append(records)
        return members_info
    
    
def recieve_Data(request):
    if(request.method == "POST"):
        reg = request.body.decode()
        
        print(type(reg))
        reg = json.loads(reg)
        
        print(type(reg), reg)
        
        return HttpResponse("OK")
    
    reg = request.method
    return JsonResponse({'foo':reg})
    
def show_member_info(request):
    connection = connect_mysql_info()
    
    records1 = connection.member_info_all()
    members_info = member.members_info(records1)
    
    records2 = connection.member_info_name()
    members_name = member.members_info(records2)
    
    records3 = connection.member_info_age()
    members_age = member.members_info(records3)
    
    connection.close_connection()
    
    template = loader.get_template('member_page.html')
    context = {
        'members': members_info, 
        'name': members_name, 
        'age': members_age
        
    }
    
    return HttpResponse(template.render(context, request))
