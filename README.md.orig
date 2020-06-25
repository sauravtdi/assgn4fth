# Activity Logger

A django based web application for logging users' active periods. To see it running, please visit [live.](https://assgn4fth.herokuapp.com/user/) 


## Description

This application showcases use of django webframework to create an application for logging users periods of activity. Logs are stored in `activity_period` table which share a foreign key with `user` table of the database. It also has a built in program based on django custom management command to populate the database with some dummy data. Finally, it has an api to serve the log data in json format. Simulation of activities such as creating users and their corressponding activity periods can be done through a web interface, access of which is provided to only admin and staff users.

### Prerequisites

Before we start, we need to clone the repository using `git clone` command. If git is not installed, we can download the project. After cloning/downloading, navigate to the root folder of the project. Create a `.env` file and assign a value to `SECRET_KEY` attribute. The `SECRET_KEY` is going to be the secret key of the django project. We can use this `.env` file to store other confidential informations such as database related credentials.

```
SECRET_KEY=ddf3gq###########
```

### Installing

A step by step series as to how to get a development environment of this application running:

#### 1. Create and activate a virtual envrionment

Create a virtualenv for our app, so open up the Command Prompt (for Windows) or Terminal (for Mac, Linux) and type the following:

```
$ virtualenv django_env
```

Use some other env name if desired. Make sure that `virtualenv` is installed. If not, use `pip install virtualenv` command to install. After installation, activate/enter the virtual environment using the below command:

```
$ source django_env/bin/activate
```

#### 2. Install all dependencies

Install all the dependencies from the `requirements.txt` file using command:
```
$ pip install -r requirements.txt
```
Make sure that all dependencies are installed correctly. Missing any would generate error in build/run phase. Django uses sqlite database that comes built in with the django package. In case, any other database is used, make sure to install corressponding dependencies and change database configuration in `settings.py` file accordingly. For more on this, please visit [this.](https://docs.djangoproject.com/en/3.0/ref/databases/)


### Running and Testing
Follow the below steps to see it running locally:

#### 1. Initial database migration

To run this application, we have to create database and tables first using command:
```
python manage.py migrate
```
This command makes sure that all relevant tables are created in the database. Note: migrate command works only when we have migration files built already in the project. Check in the user folder to see whether we have migrations folder with files such as `0001_initial.py`. If not run command `python manage.py makemigrations` before `python manage.py migrate`.

#### 2. Populating data to the database

Now that database and tables are created, let's populate the database with some dummy data using following command:

```
python manage.py populate_db n
```
Note that `n` in the above command is number of users with either `staff` or `nonstaff` authorization that we want to create. The `populate_db` program assigns random start_time and end_time(>start_time) of activity periods for every users created.    

#### 3. Run the application server

Use following command to run the server in development environment:
```
python manage.py runserver
```
This command will run the application on localhost at port 8000.

#### 4. View results

To see the users and their activity periods in json format, visit http://localhost:8000/users/.

#### 5. Check admin interface for creating more users and their activity periods - optional

Create an admin user using following command:
```
python manage.py createsuperuser
```
This command will prompt for `email`, `full name` and `password`. Once successfully created, visit http://localhost:8000/admin/ to login to the interface using the admin-user credentials. The dashboard shows the option to add/change both users and activity periods.

<<<<<<< HEAD
<<<<<<< HEAD
![alt text](/docs/img/admin_interface.png?raw=true,"admin interface")
=======
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
>>>>>>> 678e7c3616d76bbdeaf0d369f9530269c1f5bf88
=======
![alt text](/docs/img/admin_interface.png?raw=true,"admin interface")
>>>>>>> d8e590c3b2aed229d6e595746ce2eb73bb63300b

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used

## Authors

* **[Saurav Suman](https://www.linkedin.com/in/saurav-suman-980120/)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to all active community of django developers for sharing their knowledge on various platforms such as [Stack Overflow.](https://stackoverflow.com/questions/tagged/django)

