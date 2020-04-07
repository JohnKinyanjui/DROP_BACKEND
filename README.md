# DROP_BACKEND
To run server write this in terminal when in the project directory:
**run main.py**

This is a an E-commerce flask app which can be used to add stores.
A few things you can do with this api:
 * Log in Authentication.
 * User can
 * Access Token.
 * Sign up new users.
 * The user can create a store which only belongs to him/her.
 * The user can follow his or her favourite store.
 * You can add items to your store.
 * You can add data with json and also throgh endpoints
 
 
*There are a few things i want to speak about in the below picture.*


![alt text](https://github.com/JohnKinyanjui/DROP_BACKEND/blob/master/screen_shots/bar_1.JPG)

<b><i>models</i></b> - This folder is used to represent the item data and  events which help to some function like add users and stores.

<b><i>resources</i></b> - This folde  contain <b>'app.py'</b> which contains our end points.

<b><i>security</i></b> - This folder will contains python file which are responsible for log in and also to create tokens.

#Post Man
So far post man is the best software to test the api.
Tou an download post man from : https://www.postman.com/

![alt text](https://github.com/JohnKinyanjui/DROP_BACKEND/blob/master/screen_shots/post.JPG)

**Example 1**
In this example i will try to help you understand.
We can add data in our database through json and endpoints which is sqlite in folder *resources* which is called **drop_database.sqlite**.If you are using VS Code download extension called sqlite explorer to read the file in table format.

To add data through our endpoint:
 http://127.0.0.1:5000/AddStore/**1**
 
 The numeric value in the endpoint is the user  **id** and to create a store it needs to indentify the owner of the user.
 The other data in json in below image is the store info which is more ambigous or long strings so its better to add as json which is more efficient .
 
 If we look the in '**app.py**' we can see our endpont is something like this:
   api.add_resource(AddStore,'/AddStore/<int:id>')
 and   so we can see the id is represented in our enpoint and in our post man it is represented as a POST REQUEST because we are sending data.
 
![alt_text](https://github.com/JohnKinyanjui/DROP_BACKEND/blob/master/screen_shots/addstore.JPG)

Ok thats all for now for any question you can find me in facebook:

https://www.facebook.com/john.jake.754918/




