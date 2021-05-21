# to deal with json files
import json
import pandas as pd

# to store all username of top 1000 participents
userHandle_codechef = []

for i in range(0,100):
    json_file = "result."+str(i+1)+".json"
    with open(json_file) as f:
        data = json.load(f)
    
    for i in range(0,40):
        handle = data['list'][i]['username']
        userHandle_codechef.append(handle)

# print(userHandle_codechef)

# converting the list of username into a csv file 
# dictionary of lists  
dict = {'UserID': userHandle_codechef}
df = pd.DataFrame(dict)

# saving the dataframe 
df.to_csv('userID.csv')

    