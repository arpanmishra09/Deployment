from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

loaded_model=  joblib.load('diabetic_prac.pkl')


@app.route('/') #decorator
def home():
    return render_template('diabetic.html')

@app.route('/predict' , methods = ['POST']) #decorator 
def predict(): 

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass= request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    # df= pd.DataFrame(columns=['preg','plas','pres','skin','test','mass','pedi','age','status'])

    if prediction[0]==0:
        val= 'not diabetic' 
    else:
        val= 'diabetic'
    # d= {'preg':preg,'plas':plas,'pres':pres,'skin':skin,'test':test,'mass':mass,'pedi':pedi,'age':age,'status':val}
    # df= df.append(d,ignore_index='True') 
    # print(df)
    return render_template ('result.html',value= val)
if __name__=='__main__': 
    app.run(debug=True)#if debug=True is kept than the page is automatically saved each time we make chanages in the code


 