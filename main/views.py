from django.shortcuts import render
import json, psycopg2
from psycopg2 import Error
from main.models import InputList

def index(request):
    return render(request, 'main/index.html')

def data(request):
    global connection, cursor
    select_query = "SELECT * FROM main_inputlist;"
    try:
        connection, cursor = connect_to_db()

        cursor.execute(select_query)
        inputs = cursor.fetchall()
    except (Exception, Error) as error:
        return render(request, 'main/error.html', {'error': error})
    finally:
        if connection:
            cursor.close()
            connection.close()

    return render(request, 'main/data.html', {'inputs': inputs})

def submit(request):
    if request.method == 'POST':
        data = dict()
        inputs = request.POST.getlist('input', [])

        for id, value in enumerate(inputs):
            data[id] = value

        input_list = InputList(data=json.dumps(data))
        input_list.save()

        return render(request, 'main/submit.html', {'inputs': input_list.data})
    return render(request, 'main/error.html')

def connect_to_db():
    connection = psycopg2.connect(user='postgres',
                                  password='password',
                                  host='localhost',
                                  port='',
                                  database='pupa2022')

    cursor = connection.cursor()

    return connection, cursor
