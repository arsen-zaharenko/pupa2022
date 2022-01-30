# 1. install pip, postgresql, git
sudo apt update

sudo apt install -y python3-pip postgresql postgresql-contrib git
# 2. create postgresql db
sudo service postgresql start

sudo -u postgres psql

# postgres console
CREATE DATABASE pupa2022;

# change password for postgres or change user and password for database in settings.py
\password
# enter new password as 'password'

\q
# 3. create virtual enviroment
sudo pip3 install virtualenv

virtualenv django

. django/bin/activate
# 4. install django and clone project
pip install django psycopg2-binary

git clone https://github.com/arsen-zaharenko/pupa2022
# 5. make migrations and run server
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
