# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
import pickle
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        cs = float(request.form['cs'])
        mip = float(request.form['mip'])
        numunits = float(request.form['numunits'])
        oclv = float(request.form['oclv'])
        or_upb = float(request.form['or_upb'])
        olv = float(request.form['olv'])
        or_irate = float(request.form['or_irate'])
        or_lterm = float(request.form['or_lterm'])
        or_diratio=float(request.form['or_diratio'])
        hm_flag = float(request.form['hm_flag'])
        deli = float(request.form['del'])
        hm_flag_NA=0
        hm_flag_N=0
        hm_flag_Y=0
        if(hm_flag==1):
            hm_flag_NA=1
        if(hm_flag==0):
            hm_flag_N=1
        if(hm_flag==2):
            hm_flag_Y=1
        deli_N=0
        deli_Y=0
        if(deli==0):
            deli_N=1
        if(deli==1):
            deli_Y=1 
        if(cs>=0 and cs<500):
            cs_range=0
        if(cs>=500 and cs<550):
            cs_range=1
        if(cs>=550 and cs<600):
            cs_range=2
        if(cs>=600 and cs<650):
            cs_range=3
        if(cs>=650 and cs<700):
            cs_range=4
        if(cs>=700 and cs<750):
            cs_range=5
        if(cs>=750 and cs<800):
            cs_range=6
        if(cs>=800 and cs<=850):
            cs_range=7
        
        if(olv>=0 and olv<40):
            olv_range=0
        if(olv>=40 and olv<75):
            olv_range=1
        if(olv>=75 and olv<=100):
            olv_range=2
        cs=(cs-603)/219
        mip=(mip-0)/64
        numunits=(numunits-1)/3
        oclv=(oclv-46)/59
        or_upb=(or_upb-15000)/243000
        olv=(olv-46)/54
        or_irate=(or_irate-6.025)/2.305
        or_lterm=(or_lterm-357)/5
        or_diratio=(or_diratio-10)/48
        cs_range=(cs_range-0)/7
        olv_range=(olv_range-0)/2
        test_point=[[cs, mip, numunits, oclv, or_diratio, or_upb, olv, or_irate, or_lterm, hm_flag_N, hm_flag_NA, hm_flag_Y, deli_N, deli_Y, cs_range, olv_range]]
        import pandas as pd
        test_point=pd.DataFrame(test_point)
        loaded_model = pickle.load(open("model.pkl", "rb"))
        result = loaded_model.predict(test_point)
        alt1 = 'There will be no Prepayment'
        alt2 = 'There will be Prepayment'
    if result[0] == 0:
        return render_template('result.html', prediction=alt1)
    else:
        return render_template('result.html', prediction=alt2) 
    return render_template('result.html')
            
if __name__ == '__main__':
    app.run(debug=True)
