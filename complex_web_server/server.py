from flask import Flask, render_template, request, redirect
import  csv

app = Flask(__name__)
print(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        file = database.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')
        
def write_to_csv(data):
    with open('database.csv', mode='a') as csv_database:
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"],data["subject"],data["message"]])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return "Something went wrong!"