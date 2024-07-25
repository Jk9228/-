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
    for members in records:
        print(members)
    return render(request, "member_page.html" , {
        'member_name': 'jun',
        'member_age': '20'
    })
cursor.close()
connection.close()