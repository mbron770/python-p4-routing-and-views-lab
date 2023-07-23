#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_route(route): 
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number): 
    count = f''
    for n in range(number): 
        count += f'{n}\n'
    return count 

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation): 
    if operation == '+': 
        return str(num1 + num2)
    elif operation == '-': 
        return str(num1 - num2)
    elif operation == '*': 
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1/num2)
    elif operation == '%': 
        return str(num1%num2)
    
    return 'operation not recognized. Please use the one of the following: + - * div %'

# if __name__ == '__main__': 
#     app.run(port=5555)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
