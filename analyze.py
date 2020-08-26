import sys
import string
import json
import numbers
import time

from flask import Flask, request,jsonify
'''
payload_string should be a json with the following properties:
    * period    - int
    * factor    - float/double
    * data      - string (see example for the format - it should be the same format as when the observation is created)
it should terminate with EOF
'''

app = Flask(__name__)
@app.route('/', methods=['GET'])
def get():
	return '11'
def parse_value(s):
        return int(s)
@app.route('/analyze_ecg', methods=['POST'])
def main():
    period = int(request.form.get("period"))
    factor = float(request.form.get("factor"))
    data = request.form.get("data")
    if not period: raise AssertionError('period is not defined')
    if not isinstance(period, numbers.Number): raise AssertionError('period is not a number')

    if not factor: raise AssertionError('factor is not defined')
    if not isinstance(factor, numbers.Number): raise AssertionError('factor is not a number')

    if not data: raise AssertionError('data is not defined')
    if not isinstance(data, str): raise AssertionError('data is not a string')

    
    values = []
    try:
    	values = list(map(parse_value, data.split(' ')))
    	return (str(values))
    except:
    	raise AssertionError('failed to parse data into an array of integers')
    print(7.777)
    return (7.777)



if __name__ == "__main__":
        app.run(host='192.168.100.10', port=5000, debug=True)   
app.run(debug=True)
