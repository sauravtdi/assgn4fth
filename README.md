# Activity Logger

A django based web application for logging users' active periods. To see it running, please visit [live.](https://www.google.com) 


## Description

This application showcases use of django webframework to create an application for logging users periods of activity. Logs are stored in `activity_period` table which share a foreign key with `user` table of the database. It also has a built in program based on django custom management command to populate the database with some dummy data. Finally, it has an api to serve the log data in json format. Simulation of activities such as creating users and their corressponding activity periods can be done through a web interface, access of which is provided to only admin and staff users.


### Installing

A step by step series as to how to get a development env of this application running:

#### 1. Create and activate a virtual envrionment

Before we start, we need to create a virtualenv for our app, so open up your Command Prompt (for Windows) or Terminal (for Mac, Linux) and type the following:
```
$ virtualenv django_env
```

Use some other env name if you want to. Make sure that `virtualenv` is installed. If not use `pip install virtualenv` to install. After installation, activate/enter the virtual environment using the below command:

```
$ source django_env/bin/activate
```

#### 2. Install all dependencies

Install all the dependencies from the `requirements.txt` file using command:
```
pip install -r requirements.txt
```
Make sure that all dependencies are installed correctly. Missing any would generate error in build/run phase. Django uses sqlite database that comes built in with the django package. In case, any other database is used, make sure to install corressponding dependencies and change database configuration in `settings.py` file accordingly. For more on this, please visit [this.](https://docs.djangoproject.com/en/3.0/ref/databases/)


### Running and Testing

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used

## Authors

* **[Saurav Suman](https://www.linkedin.com/in/saurav-suman-980120/)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to all active community of developers for sharing their knowledge on platforms such as Stack Overflow.

