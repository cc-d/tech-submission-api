To run:

install uvicorn
pip3 install -r requirements.txt

Then start w/ uvicorn
uvicorn run:app --host 0.0.0.0 --port 8000

To use:
	Register a new user: http://168.235.89.157:8000/register?username=USERNAME&password=PASSWORD
	Example: http://168.235.89.157:8000/register?username=a&password=a


	Add new contact: http://168.235.89.157:8000/add_contact
	Parameters: username, first name, last name, numbers (JSON string), city, state, zip code

	Example:
	Contact Numbers: {'mobile':['1234', '5678'], 'home:['1111']}
	
	Example URL:
	http://168.235.89.157:8000/add_contact?user=USERNAME&numbers={%27mobile%27:[%27555-0000%27,%27555-0001],%27home%27:[%27555-1111%27]}&first=fname&last=lname&city=c&state=tn&zip_code=12345
	Example: http://168.235.89.157:8000/add_contact?user=a&numbers={%27mobile%27:[%27555-0000%27,%27555-0001],%27home%27:[%27555-1111%27]}&first=fname&last=lname&city=c&state=tn&zip_code=12345



