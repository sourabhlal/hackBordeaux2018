from flask import Flask, request, abort, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/play', methods=['GET'])
def joinGame():
    return render_template('client_template.html', name="john")
    # return 'hello world! we are at hack bordeaux', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
