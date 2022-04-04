Preface:

A LOT of things do not handle edge cases, return everything I'd like to return, etcetcetc. I've tried to remember and comment in places where I only did something in a specific way to save time, but would never do such a thing in an actual app, but there may have been a few things I missed (including .gitignore, file structures, and so on). I'll include an example database with already registered users in the uploaded directory, but any data included in the sqlite3

___

Requirements:

sqlite 3
on ubuntu 20 "apt-get install sqlite"

python 3
on ubuntu 20 "apt-get install python3"

pip
on ubuntu 20 "apt-get install python3-pip"

uvicorn
on ubuntu 20 "apt-get install uvicorn"

all flask/python requirements
on ubuntu 20 "pip3 install -r requirements.txt"


____

To use:

start w/ uvicorn in root directory
uvicorn run:app --host 0.0.0.0 --port 8000

navigate to: http://[YOUR IP HERE]:8000/
____

Endpoints:

Register a new user: GET http://168.235.89.157:8000/register?username=USERNAME&password=PASSWORD (IN A REAL APP I WOULD __NOT__ HAVE THE PASSWORD IN A QUERY STRING)
Example: http://168.235.89.157:8000/register?username=a&password=a

Response:

```
{"success":"ok"}
```
-

Add new contact: GET http://168.235.89.157:8000/add_contact
Parameters: username, first name, last name, numbers (JSON string), city, state, zip code

Example:
Contact Numbers: {'mobile':['1234', '5678'], 'home:['1111']}

Example URL:
http://168.235.89.157:8000/add_contact?user=a&numbers={%27mobile%27:[%27555-0000%27,%27555-0001],%27home%27:[%27555-1111%27]}&first=fname&last=lname&city=c&state=tn&zip_code=12345

Response:

```
{"success":"ok"}
```

-

Get a user token: POST http://168.235.89.157:8000/token

Response:

```{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhIiwiZXhwIjoxNjQ5MTA1MDg4fQ.mkOGeo1xdkZEGTxbhk-VrZRyjK724xqW6RxtiykEjhQ",
    "token_type": "bearer"
}```