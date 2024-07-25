from django.shortcuts import render
import mysql.connector
# Create your views here.

connection = mysql.connector.connect(host='localhost', port='3306',
user='Jk9228', password='1234')

cursor = connection.cursor()

cursor.execute("use ooschool;")

cursor.execute("SELECT * FROM member ORDER BY age DESC limit 3;")
records = cursor.fetchall()



def show_member_info(request):
    members_info = []
    for member in records:
        members_info.append({member[0], member[1]})  
        
    return render(request, "member_page.html", {
        'members': members_info
    })
cursor.close()
connection.close()