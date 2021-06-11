# 2021-1 Open Source Software Lab Final Project

## 21300717 Huiwon Jeong

## What does this project do?
This project is designed to help you register for class.\
If there is a vacancy in the class, you can receive a notification via email. \n

## Structure & Process
A simple web server was implemented through an open-source web framework, "Flask", and the web was used to receive the necessary information from the user.
If you enter information about the class you want to enroll in via the web, the program reads the number of students currently enrolled in the class and limit number of students through crawling. After pressing a button on the web, all processes are implemented to operate through thread.

## Set up & Usage
To install the required Python package, run the command below.
```
$ sudo apt-get update
$ sudo pip install -r requirements.txt
```

