--This webapp runs on port number 8080.
--The user will have to install virtual environment to be able to run the webapp.

	If you are on Mac OS X or Linux, chances are that the following command will work for you:

	$ sudo pip install virtualenv
	It will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:

	$ sudo apt-get install python-virtualenv
	If you are on Windows and don’t have the easy_install command, you must install it first. Once you have it installed, run the same commands as above, but without the sudo prefix.

--Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:

	$ mkdir myproject
	$ cd myproject
	$ virtualenv venv
	New python executable in venv/bin/python
	Installing setuptools, pip............done.
--Now, you only have to activate the corresponding environment. On OS X and Linux, do the following:

	$ . venv/bin/activate
	If you are a Windows user, the following command is for you:

	$ venv\Scripts\activate
	Either way, you should now be using your virtualenv.
--Other than this you will have to install the requests module, flask module, render_template:
	$ pip install Flask
	$ pip install requests
	$ pip install render_template

Just pull the code into the above directory.
Open command prompt/terminal and run the 'app.py'. Your app would be working on port 8080!
Cheers!
These are the endpoints for which the webapp work:
--http://localhost:8080/ that displays "Hello World!"

--http://localhost:8080/authors, which:
-fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users

--http://localhost:8080/posts,which: 
-fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts

--http://localhost:8080/count-posts,which:
-Responds with only a list of authors and the count of their posts (a newline for each author).

--http://localhost:8080/setcookie which sets a cookie

--http://localhost:8080/getcookies fetches the set cookie.

--http://localhost:8080/robots.txt page is denied

--http://localhost:8080/html renders an html page

--http://localhost:8080/input displays an input box that takes input values and print it on stdout and the webpage.
	

