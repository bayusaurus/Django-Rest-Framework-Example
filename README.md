# Tools I use
- Python 3.8
- MySQL 8.0

# How To Use
1. Clone this repository
2. Configure Database
- Create new blank database
- Configure database in settings.py with the setting same as database in your local machine
3. Configure Env
- Create new Env 
```bash
py -m venv your-env-name
```
- Activate created Env
```bash
.\your-env-name\scripts\activate
```
- Install Env from requirements.txt using the activated Env, change directory to this django app directory
```bash
pip install -r requirements.txt
``` 
4. Migrate and Run
- Using the activated Env change directory to this django app directory
- Do the migration
```bash
py manage.py migrate
```
- Run the application
```bash
py manage.py runserver
```
-Try the application in localhost:8000

## About The Application

- If you want to add data via django admin you can first create django superuser
```bash
py manage.py createsuperuser
```
and then fill the data and then you can visit localhost:8000/admin

- you can check the api documentation in localhost:8000/api/playground/
- you also can check the api via postman using Article Api Collection.postman_collection.json
