# 파일명 : getcookiesv.py
# python flask server

# _*_ coding: utf-8 _*_
from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def index():
	r = request.args.get('cookie')
	return 'return'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=1234)