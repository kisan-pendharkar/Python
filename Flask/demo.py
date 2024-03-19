from flask import Flask
from cal import add,mul,div,sub

app=Flask(__name__)

@app.route('/add')
def add_fun():
	result=add()
	return "Addition :"+str(result)

@app.route('/sub')
def sub_fun():
	result=sub()
	return "Substracton :"+str(result)

@app.route('/mul')
def mul_fun():
	result=mul()
	return "Multiplication :"+str(result)


@app.route('/div')
def div_fun():
	result=div()
	return "Divsion :"+str(result)



if __name__=='__main__':
	app.run(debug=True,port=9123)