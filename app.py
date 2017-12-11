from flask import Flask, render_template,make_response, request, abort
import requests


app=Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
	return "Hello World- Gauri"



@app.route('/authors')
def authors():
	res = requests.get('https://jsonplaceholder.typicode.com/users',None)
	resDict = res.json()
	print('response from server:'+ res.text)
	authors_list=resDict[0]['name']
	for i in range(1,len(resDict)):
		authors_list=authors_list + '<br>'+resDict[i]['name']
	return authors_list


@app.route('/posts')
def posts():
	res=requests.get('https://jsonplaceholder.typicode.com/posts',None)
	postDict=res.json()
	print('response from server'+res.text)
	count=0;
	for i in range (len(postDict)):
		count=count+1
	count=str(count)
	return count

@app.route('/count-posts')
def count_posts():
	res=requests.get('https://jsonplaceholder.typicode.com/posts',None)
	postDict=res.json()
	res = requests.get('https://jsonplaceholder.typicode.com/users',None)
	resDict = res.json()
	count_list=""
	for i in range (len(resDict)):
		count=0
		for j in range(len(postDict)):
			if(resDict[i]['id']==postDict[j]['userId']):
				count=count+1
		count_list=count_list + '<br>'+resDict[i]['name']+'  '+str(count)
	
	return count_list


@app.route('/setcookie')
def setcookie():
	resp = make_response('Setting cookie')
	resp.set_cookie('name','Gauri')
	resp.set_cookie('age','20')
	return resp

@app.route('/getcookie')
def getcookie():
   name=request.cookies.get('name')
   age=request.cookies.get('age')
   return 'The name is '+name+'<br> The age is '+age

@app.errorhandler(404)
def page_not_found(error):
    return 'Work in Process',404

@app.route('/robots.txt')
def robots_txt():
	return "You aren't allowed to access this file. <br/>Contact the system administrator.", 403


@app.route('/html')
def index():
	return render_template('Index.html')
	
@app.route('/input')
def input():
	return render_template('input_box.html')

@app.route('/input', methods=['POST'])
def input_post():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    return processed_text

if __name__=='__main__':
	app.run(port=8080)