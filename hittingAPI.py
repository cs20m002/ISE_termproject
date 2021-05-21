import requests
import pprint
import csv
import json

http = "https://competitive-coding-api.herokuapp.com/api/codechef/"


i=1
j=644
# reading userID from the csv file 
with open('userID.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if i<=644:
            i+=1
            continue
        url = http
        url += row[1] # full url to hit the API 
        # print(url)
        response = requests.get(url) 
        json_response = response.json()
        # print(type(json_response))
        
        
        #saving into json format
        output = "user"
        output += str(j)
        output += ".json"
        j += 1
        with open(output, "w") as outfile: 
            json.dump(json_response, outfile)
        # break
        
        