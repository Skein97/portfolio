from flask import Flask, url_for, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def start():
    return render_template('index.html')

@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('database.csv', 'a', newline='') as database:
                csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL).writerow( [data["email"], data["subject"],data["message"]])
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong try again'



# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

