<!-- create project -->

mkdir app

cd app

python3 -m venv env

source env/Scripts/activate

pip install Flask Flask-SQLAlchemy

pip install -U flask-cors

pip install flask-mysql

pip install flask-restful

pip install mysqlclient 

<!-- start project -->

cd app

source env/Scripts/activate

Flask run