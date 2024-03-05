from flask import Flask, render_template, request

import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    matches = re.finditer(regex_pattern, test_string)
    matches_info = [{'match': match.group(), 'position': match.start()} for match in matches]
    
    return render_template('results.html', test_string=test_string, regex=regex_pattern, matches=matches_info)

if __name__ == '__main__':
    app.run(debug=True)
