from flask import Flask, request, abort, render_template
from datetime import datetime
app = Flask(__name__)

clues = []
views = []

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
    template_variables = {}
    template_variables["clues"] = clues
    template_variables["views"] = views
    if len([d for d in clues if d['discoverd'] == False])%2 == 1:
        template_variables["clue_odd"] = True
    else:
        template_variables["clue_odd"] = False
    return render_template('client_template.html', tv=template_variables)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
