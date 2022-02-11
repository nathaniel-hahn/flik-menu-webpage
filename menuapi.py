from flask import Flask, json, request, make_response
from flask_cors import CORS
import requests
import datetime
from datetime import date



today = date.today() #menu api date setup
tomorrow = datetime.date.today() + datetime.timedelta(days=1) #tomorrow set up
d3 = today.strftime("%y/%m/%d")
wd = tomorrow.weekday()


breakfast_menu = ["no item found", "no item found", "no item found", "no item found"]
lunch_menu = ["no item found", "no item found", "no item found", "no item found"]
dinner_menu = ["no item found", "no item found", "no item found", "no item found"]
new_menu = []

def getmenu():
    breakfast = requests.get(
        'https://stevensonschool.flikisdining.com/menu/api/weeks/school/stevenson-school/menu-type/breakfast/20' + str(
            d3))
    lunch = requests.get(
        'https://stevensonschool.flikisdining.com/menu/api/weeks/school/stevenson-school/menu-type/lunch/20' + str(d3))
    dinner = requests.get(
        'https://stevensonschool.flikisdining.com/menu/api/weeks/school/stevenson-school/menu-type/dinner/20' + str(d3))

    print(breakfast.status_code)
    for x in range(1, 5): #making sure missed meals are ignored and different amounts of food
        try:
            breaky = breakfast.json()["days"][wd]["menu_items"][x]["food"]["name"]
            breakfast_menu.insert(0, str(breaky))
            print(breaky)
        except:
            pass
        try:
            lunchy = lunch.json()["days"][wd]["menu_items"][x]["food"]["name"]
            lunch_menu.insert(0, str(lunchy))
            print(lunchy)

        except:
            pass
        try:
            din_din = dinner.json()["days"][wd]["menu_items"][x]["food"]["name"]
            dinner_menu.insert(0, str(din_din))
            print(din_din)
        except:
            pass

    
    for i in range(0, 3):
        breakfast_menu.append("no item found")
        lunch_menu.append("no item found")
        dinner_menu.append("no item found")
        
    print(breakfast_menu)
    print(lunch_menu)
    print(dinner_menu)
    new_menu.append(breakfast_menu)
    new_menu.append(lunch_menu)
    new_menu.append(dinner_menu)

    print(new_menu)

api = Flask(__name__)
CORS(api)
@api.route('/menuapi', methods=['GET'])
def get_companies():
  new_menu.clear()
  lunch_menu.clear()
  breakfast_menu.clear()
  dinner_menu.clear()
  getmenu()
  menu = {
    "breakfast":[
    {"item":new_menu[0][0]},
    {"item":new_menu[0][1]},
    {"item":new_menu[0][2]},
    {"item":new_menu[0][3]}

    ],
    "lunch": [
    {"item":new_menu[1][0]},
    {"item":new_menu[1][1]},
    {"item":new_menu[1][2]},
    {"item":new_menu[1][3]}

    ],
    "dinner":[
    {"item":new_menu[2][0]},
    {"item":new_menu[2][1]},
    {"item":new_menu[2][2]},
    {"item":new_menu[2][3]}

    ]

}

  response = make_response(json.dumps(menu))
  response.headers.add('Access-Control-Allow-Origin', '*')

  return response

if __name__ == '__main__':
    api.run() 
