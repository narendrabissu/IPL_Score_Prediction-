import pandas as pd
import numpy as np
import re
import joblib
import sys
with open('regression_model.joblib','rb') as f:
    linearRegressor=joblib.load(f)

def predict_runs(test_case) :
   with open('regression_model.joblib','rb') as f:
    linearRegressor=joblib.load(f) 
    with open('venue_encoder.joblib','rb') as f:
      venue_encoder=joblib.load(f)
    with open('team_encoder.joblib','rb') as f:
      team_encoder=joblib.load(f)
    test_case=pd.read_csv(test_case)
    Array=test_case.to_numpy()
    Array.reshape(-1,1)
    test_case['venue']=venue_encoder.fit_transform(test_case['venue'])
    test_case['batting_team']=venue_encoder.fit_transform(test_case['batting_team'])
    test_case['bowling_team']=venue_encoder.fit_transform(test_case['bowling_team'])
    test_case['wickets']=len(re.split(',',list(test_case['batsmen'])[0]))
    test_case=test_case[['venue','innings','batting_team','bowling_team','wickets']]
    return linearRegressor.predict(test_case)
