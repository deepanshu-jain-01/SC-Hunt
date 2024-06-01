from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import firebase_admin
from firebase_admin import credentials, db, auth
from firebase import Firebase
import ast
from Filter_Query import filter, sorting, shuffle, search


config1 = {
  "apiKey": "AIzaSyA7eiVdQ9EJbNH4mSwdAyUjq9aVrzqUIIY",
  "authDomain": "schunt1-ae447.firebaseapp.com",
  "databaseURL": "https://schunt1-ae447-default-rtdb.firebaseio.com",
  "projectId": "schunt1-ae447",
  "storageBucket": "schunt1-ae447.appspot.com",
  "messagingSenderId": "882788594359",
  "appId": "1:882788594359:web:8ce141d26e12a949da5332",
  "measurementId": "G-2PCH7K1L52"
}
# sc hunt 2
config2 = {
  "apiKey": "AIzaSyDnnd2Yd8-eIaQDeZujqr34DSfI0gAwFp0",
  "authDomain": "schunt2.firebaseapp.com",
  "databaseURL":"https://schunt2-default-rtdb.firebaseio.com/",
  "projectId": "schunt2",
  "storageBucket": "schunt2.appspot.com",
  "messagingSenderId": "219423670204",
  "appId": "1:219423670204:web:2cbcd89b735489bb1d75b9"
  }
# sc hunt 3
config3 = {
  "apiKey": "AIzaSyBe3WOQG5Wi2RIqrboQQkAYaQ6j0SP0NpQ",
  "authDomain": "schunt3-328c3.firebaseapp.com",
  "databaseURL": "https://schunt3-328c3-default-rtdb.firebaseio.com",
  "projectId": "schunt3-328c3",
  "storageBucket": "schunt3-328c3.appspot.com",
  "messagingSenderId": "190311952863",
  "appId": "1:190311952863:web:ba47108d9c0a42cf6c546a"
}

Config = {
  "apiKey": "AIzaSyBsVWHQpxYKD9On0X0CQf2zkscYjziZ0T8",
  "authDomain": "userdb-b3349.firebaseapp.com",
  "databaseURL": "https://userdb-b3349-default-rtdb.firebaseio.com",
  "projectId": "userdb-b3349",
  "storageBucket": "userdb-b3349.appspot.com",
  "messagingSenderId": "225172549895",
  "appId": "1:225172549895:web:96bbf7403667a2bfcad5a2"
}

default_states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE",
    "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
    "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
    "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
    "NC", "ND", "OH", "OK", "OR", "PA", "RI",
    "SC", "SD", "TN", "TX", "UT", "VT", "VA",
    "WA", "WV", "WI", "WY"
]

default_job_types = [
    "Full Time", "Part Time", "Temporary/Contract"
]

user_firebase = Firebase(Config)
firebase1 = Firebase(config1)
firebase2 = Firebase(config2)
firebase3 = Firebase(config3)


app = Flask(__name__)
app.secret_key="Djjain844"

global uid_global
global original
uid_global = None

@app.route('/')
def start():
    return render_template("cover.html")

@app.route('/api/user_details', methods=['POST'])
def get_data():
    user_db = user_firebase.database()
    global uid_global
    rec_data = request.json
    input_key=rec_data["uid"]
    uid_global=input_key
    data={"mail":rec_data["email"],"applied_jobs":["SAMPLE","SAMPLE2"],"comments":["SAMPLE","SAMPLE2"]}
    user_db.child(input_key).set(data)

@app.route('/index/<user_id>')
def index(user_id):
    global uid_global
    uid_global = user_id
    user_db = user_firebase.database()
    db1 = firebase1.database()
    db2 = firebase2.database()
    db3 = firebase3.database()
    part_1 = db1.get()
    part_2 = db2.get()
    part_3 = db3.get()
    IDS=user_db.child(uid_global).get().val()['applied_jobs']
    total = {}
    for item in part_1.each():
      total[str(item.key())]=item.val()
    for item in part_2.each():
      total[item.key()]=item.val()
    for item in part_3.each():
      total[item.key()]=item.val()
    
    global original
    original = shuffle(total)
    i=0
    total = {}
    for k,v in original.items():
        if i==30:
            break
        else:
            i=i+1
            total[k]=v
    return render_template('index.html', data=total, user_id=user_id, applied_ids=IDS)

@app.route('/application/', methods=['POST'])
def apply_job():
        global uid_global
        KEY = uid_global
        
        user_db = user_firebase.database()
        if request.method == "POST":
            IDS = ast.literal_eval(request.form.get("total_jobs"))    
            ID = request.form.get("apply_id")
            d_total = ast.literal_eval(request.form.get("total_data"))
            IDS.append(ID)
            user_db.child(KEY).update({"applied_jobs":IDS})
        
            return render_template('index.html', data=d_total, user_id=KEY, applied_ids=IDS)
        
@app.route('/filtering', methods=['POST'])
def filtered_results():
        global uid_global
        global original
        KEY = uid_global 
        #user_db = user_firebase.database()
        if request.method == "POST":
            IDS = ast.literal_eval(request.form.get("total_jobs"))
            #d_total = ast.literal_eval(request.form.get("total_data"))
            locations = request.form.getlist('state')
            job_type = request.form.getlist('job_type')
            sort_way = request.form.get('alpha_sort')
            output_data=filter(original,locations,job_type)

            if sort_way is not None:
                if sort_way == 'ascending':
                    output_data=sorting(output_data,'job_title',False)
                else:
                    output_data=sorting(output_data,'job_title',True)
          
            return render_template('index.html', data=output_data, user_id=KEY, applied_ids=IDS)


@app.route('/searching', methods=['POST'])
def search_results():
       global uid_global
       global original
       KEY = uid_global   
       #user_db = user_firebase.database()
       if request.method == "POST":
           IDS = ast.literal_eval(request.form.get("total_jobs"))    
           ID = request.form.get("apply_id")
           #d_total = ast.literal_eval(request.form.get("total_data"))
           keyword = request.form.get('keyword_filter')
           output_data = search(original, keyword)
           return render_template('index.html', data=output_data, user_id=KEY, applied_ids=IDS)
       
@app.route('/track', methods=['POST'])
def track_jobs():
    global original
    if request.method=="POST":
        IDS = ast.literal_eval(request.form.get("total_jobs"))
        temp = []
        for id in IDS:
            if id=="SAMPLE" or id=="SAMPLE2":
                pass
            else:
                temp.append(original[id])
        return render_template("dashboard.html",data=temp)
    return render_template("dashboard.html",data=temp)

@app.route('/goback')
def gotoindex():
    global uid_global
    KEY=uid_global
    return render_template("index.html",user_id=KEY)
    
if __name__ == '__main__':
    app.run(debug=True)

##########################################333
