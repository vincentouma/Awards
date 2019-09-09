# Awards


## Description
This application that allows a user to post their projects they have created and get them reviewed by fellow peers and vote according to how they feel towards a particular project.
## BDD
| Behaviour                                                                   | Input                                        | Output                                                              |
|-----------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------|
|  The Page loads the homepage                                                |  On application load                         |  Navigate to the home/index page displaying all the projects        |
|  Navigate to signup page when SignUp is clicked on the navigation bar:      |  User successfully registers                 |  User redirected to the login page                                  |
|  Navigate to the login page when Login is clicked on the navigation bar:    |  Click on Login on the Navbar dropdown menu  |  User can view a specific image with all its details                |
|  User is redirected to the specific profile page                            |  User clicks on profile icon                 |  User Redirected to the index page which displays all projects      |
|  The program directs the user to a review page with a single project details and vote button: 	|  Click on Review Project 	|  User redirected to the single project review page with the project's description and a vote button|
|  Program navigates to the vote modal form 	                              |  Click on Vote button 	                     |  A vote modal form pops up                                          |
|  Program should load the live site on a new tab 	                          |  Click on View Site/Live Project Link       	|  Live site of a specific project loads                           |
|  User is redirected to the Profile Page                                  	|  User clicks Profile on the Navbar dropdown   	|  Program opens Profile page with all users information including their projects   |



## Specifications
- Search Feature to search for projects.
- Visit actual site.
- Admin Dashboard that allows managing of the application.


## Setup/Installation Requirements

### Clone the Repo
Run the following command on the terminal:
- git clone https://github.com/vincentouma/Awards && cd Award

### Activate virtual environment

Activate virtual environment using python3.6 as default handler

```sh
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependencies

Install dependencies that will create an environment for the app to run

```sh
pip3 install -r requirements.txt
```

### Create the Database

```sh
psql
CREATE DATABASE insta;
```

### .env file
Create .env file and paste paste the following filling where appropriate:

```python
SECRET_KEY = '<Secret_key>'
DBNAME = ''
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```

### Run initial Migration
```sh
python3.6 manage.py makemigrations
python3.6 manage.py migrate
```

### Run the app
```sh
python3.6 manage.py runserver
```
#### Open terminal on
```sh
localhost:8000
```

## Known Bugs
  -No known bugs.  

## Technologies used

```sh
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- Postgressql
- Heroku
```

## Support and contact details
 - Email Address: vincoumah@gmail.com

## Link to deployed site
  https://vinaward.herokuapp.com/


## License and terms of use

[MIT License](license) this application's source code is free for any open source projects


