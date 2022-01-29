from django.shortcuts import render
import json, psycopg2
from psycopg2 import Error

def index(request):
    return render(request, 'main/index.html')

def data(request):
    global connection, cursor
    inputs = []
    select_query = "SELECT * FROM inputs;"
    create_table_query = "CREATE TABLE inputs (ID SERIAL PRIMARY KEY, data JSONB);"
    try:
        connection, cursor = connect_to_db()

        cursor.execute(select_query)
        inputs = cursor.fetchall()
    except (Exception, Error) as error:
        if "does not exist" in str(error):
            connection, cursor = connect_to_db()

            cursor.execute(create_table_query)
            connection.commit()
        else:
            return render(request, 'main/error.html', {'error': error})
    finally:
        if connection:
            cursor.close()
            connection.close()

    return render(request, 'main/data.html', {'inputs': inputs})

def submit(request):
    global connection, cursor
    if request.method == 'POST':
        data = dict()
        inputs = request.POST.getlist('input', [])

        for id, value in enumerate(inputs):
            data[id] = value

        create_table_query = "CREATE TABLE inputs (ID SERIAL PRIMARY KEY, data JSONB);"
        insert_query = f"INSERT INTO inputs (DATA) VALUES ('{json.dumps(data)}');"

        try:
            connection, cursor = connect_to_db()

            cursor.execute(create_table_query)
            connection.commit()

            cursor.execute(insert_query)
            connection.commit()
        except (Exception, Error) as error:
            if "already exists" in str(error):
                connection, cursor = connect_to_db()

                cursor.execute(insert_query)
                connection.commit()
            else:
                return render(request, 'main/error.html', {'error': error})
        finally:
            if connection:
                cursor.close()
                connection.close()

        return render(request, 'main/submit.html', {'inputs': data})
    return render(request, 'main/error.html')

def connect_to_db():
    connection = psycopg2.connect(user='postgres',
                                  password='password',
                                  host='localhost',
                                  port='',
                                  database='pupa2022')

    cursor = connection.cursor()

    return connection, cursor