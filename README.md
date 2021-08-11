# FoodKart

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Illustrations](#illustrations)
* [Contributers](#contributors)

## General info
This is a food aggregrator application (eg:-Uber eats,Swiggy) .The main application includes features like search your favourite food, add to cart, Location tracking of your orders in real-time, check your past orders etc. 

## Technologies
Project is created with:
* HTML,CSS,BOOTSTRAP
* Django
* Javascript
* Firebase

## Setup
To run this project, Clone this repo to your desktop:

- Create a firebase database and paste your credentials in [this file](./foodkart/static/js/firebase-example.js?raw=true)
- Rename  [this file](./foodkart/static/js/firebase-example.js?raw=true) to 'firebase.js' 
- Execute the following commands from your command line/terminal:
```
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Features
### For User
- Signin/Signout
- Search food
- Add to cart
- Place orders
- Track order status and location in Real-time
### For Restaurants
- Signin/Signout
- Real-time updates on orders
- Update Order status
- Add,Delete and update Menu
### For Delivery Exec
- Signin/Signout
- View Orders list under a range
- Track the own, restaurant and customer location location

## Illustrations
![Alt text](/examples/eg1.jpg?raw=true)
![Alt text](/examples/eg2.jpg?raw=true)
![Alt text](/examples/eg3.jpg?raw=true)
![Alt text](/examples/eg4.jpg?raw=true)

## Contributors

- [Yash Bontala](https://github.com/Yashbontala)
- [Jyotishna Baishya](https://github.com/JyotishnaBaishya)
- [Amit Kumar](https://github.com/amit295-cse)
- [Anikeit Sethi](https://github.com/sanikeit)
