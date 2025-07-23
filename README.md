# We-write-Yandex.Afisha
## About the project
A site with an interactive map of Moscow, where the types of active recreation are marked with detailed descriptions.
## Environment variables
Some of the project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in the format: `VARIABLE=value`.

- `DEBUG`:
This variable specifies whether the application is in debug mode. If DEBUG is True, the application will print detailed error messages and other debugging information. In a production environment, this value should be False to avoid leaking information about the internal structure of the application.

- `ALLOWED_HOSTS`:
This is a list of domain names and IP addresses from which your application can accept requests. In a production environment, you only need to specify the hosts from which your application should accept requests.

- `DB_ENGINE`:
This variable specifies the type of database you are using (e.g. PostgreSQL, MySQL, SQLite, etc.). Built-in database servers in Django:
```
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'
```
It defines which driver will be used to connect to the database.

- `DB_NAME`:
This is the name of the database your application will connect to. Depending on the database engine you are using, this may be the name of a specific database created for your application.

- `SECRET_KEY`:
This is a string used to secure your application. In Django, for example, it is used for operations such as token creation and data encryption.
It can be obtained as follows:
```
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```

## How to run
This project is developed on version `Python 3.12.5`

### Download this project
To download the project from GitHub, you can use one of the following methods:

1. Downloading a ZIP archive

- Go to the repository page on GitHub.
- Click the "Code" button in the upper right corner.
- Select "Download ZIP" from the drop-down menu.
- Once the download is complete, unzip the ZIP archive on your computer.

2. Cloning a repository with Git

If you have Git installed, you can clone the repository using the command line:
- Open a terminal (or command line).
- Go to the directory where you want to download the project.
- Enter the command:
`git clone https://github.com/username/repository.git`
Replace username with the username of the repository owner, and repository with the name of the repository.
- Press Enter, and Git will download the project to your computer.

3. Using GitHub Desktop

If you prefer a graphical interface, you can use GitHub Desktop:
- Install GitHub Desktop if you don't have it already.
- Open GitHub Desktop and sign in to your GitHub account.
- Click "File" > "Clone repository".
- Select the repository you want to download and click "Clone".
  
### Install dependencies
For the project to work, you need to install dependencies. This can be done by entering the command:
```
pip install -r requirements.txt
```

### Finishing the project setup
- Create a database file and immediately apply all migrations with the command:
```
python3 manage.py migrate
```
- Create and fill in environment variables
- Run the server with the command:
```
python3 manage.py runserver
```

## Automated adding of places
To add new places, use the script `load_place.py`
How to use:
```
python manage.py load_place (arguments)
```
### Arguments
- -u / --url:
Importing place data by reference to a JSON file. Example:
```
python manage.py load_place --url https://example.com/place.json
```
- -p / --path:
Importing place data from a local JSON file. Example:
```
python manage.py load_place --path ./data/place.json
```

### What the JSON file should look like
The JSON file should contain the following structure:
```
{
  "title": "Название места",
  "description_short": "Краткое описание",
  "description_long": "Полное описание",
  "coordinates": {
    "lat": 55.751244,
    "lng": 37.618423
  },
  "imgs": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}
```
