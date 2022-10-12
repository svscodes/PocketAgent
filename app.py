from flask import Flask, render_template,request
app = Flask(__name__)

topLocation = dict({"Delhi": ["laal kial","modi"], "Chennai": ["Beach","Parthasarathy Temple","hgfd"]})

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/agenda',methods=['POST'])
def timetable():
   result = request.form
   print(result["location"])
   print(topLocation[result["location"]])
   chosenLocation = topLocation[result["location"]]
   return render_template('agenda.html',chosenLocation = chosenLocation  )




if __name__ == '__main__':
   app.run()

