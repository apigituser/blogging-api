# Blogging-API (In-Progress)
An API that allows users to create blogs and store them in a database 

## Features
1. Create blog
2. Fetch all the blogs
3. Fetch a single blog
4. Update a blog
5. Delete a blog

## Database Setup
Refer to Django's Documentation to setup your preferred database  
```
https://docs.djangoproject.com/en/5.2/ref/databases/
```

## Installation
Clone this repository  
```
git clone https://github.com/apigituser/blogging-api
```
Navigate to blogging-api directory/folder and install the requirements
```
pip install -r requirements.txt
```
Modify the DATABASES variable in settings.py to configure your own database
```
DATABASES = {
  your database settings
}
```

## Usage
Make the migrations
```
python manage.py makemigrations
```
Run the migrations
```
python manage.py migrate
```
Run the django app using the following command
```
python manage.py runserver
```

## Roadmap.sh Project URL
Project link is available [here](https://roadmap.sh/projects/blogging-platform-api)
