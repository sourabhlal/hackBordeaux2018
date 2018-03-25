from flask import Flask, request, abort, render_template
from datetime import datetime
import json
app = Flask(__name__)

views=[{"id":"Restart_game",
        "filename":"images/bedroom.jpg",
        "title":"Bedroom",
        "discovered":False
        },
        {"id":"Start_Game",
        "filename":"images/bedroom.jpg",
        "title":"Bedroom",
        "discovered":False
        },
        {"id":"Hallway",
        "filename":"images/hallway.png",
        "title":"Hallway",
        "discovered":False
        },
        {"id":"Elevator",
        "filename":"images/elevator_inside.jpg",
        "title":"Elevator",
        "discovered":False
        },
        {"id":"Staircase",
        "filename":"images/staircase.jpg",
        "title":"Staircase",
        "discovered":False
        },
        {"id":"Exit",
        "filename":"images/exit_success.jpg",
        "title":"Exit",
        "discovered":False
        }]

clues=[{"id":"Bed",
        "filename":"images/ekino.jpg",
        "title":"Paper",
        "discovered":False
        },
        {"id":"Mobile_phone",
        "filename":"images/phone.jpg",
        "title":"Mobile phone",
        "discovered":False
        },
        {"id":"Sock",
        "filename":"images/sock.jpg",
        "title":"Sock",
        "discovered":False
        },
        {"id":"Visit_card",
        "filename":"images/visit_card.jpg",
        "title":"Visit card",
        "discovered":False
        },
        {"id":"Wardrobe",
        "filename":"images/try_again.jpg",
        "title":"Paper",
        "discovered":False
        }]

current_view={}

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
    template_variables["clues"] = [c for c in clues if c['discovered'] == True]
    template_variables["current_view"] = current_view["filename"]
    if len([d for d in clues if d['discovered'] == False])%2 == 1:
        template_variables["clue_odd"] = False
    else:
        template_variables["clue_odd"] = True
    return render_template('client_template.html', data=template_variables)

import pprint
pp = pprint.PrettyPrinter(indent=4)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        j = json.dumps(request.json)
        found = json.loads(j)["result"]["metadata"]["intentName"]
        tempList = clues+views
        for i in tempList:
            if i["id"] == found:
                i["discovered"] = True
                current_view = i
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
