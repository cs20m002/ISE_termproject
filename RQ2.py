import json

same_trend = 0
opps_trend = 0

for i in range(0,1000):
    json_file = "user"+str(i+1)+".json"
    with open(json_file) as f:
        data = json.load(f)

        keyErrorHandling1 = data.get("message")
        keyErrorHandling2 = data.get("status")

        if keyErrorHandling1 == "Internal Server Error" :
            pass
        elif keyErrorHandling2 == "Failed":
            pass
        else :
            long1,long2 = 0,0
            short1, short2 = 0,0
            for i in range(0,len(data["contest_ratings"])):
                if data["contest_ratings"][i]["code"][:4] == "COOK" and int(data["contest_ratings"][i]["rating"]) < 1800 :
                    short1 += 1
                elif data["contest_ratings"][i]["code"][:4] == "LTIM" and int(data["contest_ratings"][i]["rating"]) < 1800 :
                    short1 += 1
                elif data["contest_ratings"][i]["code"][:4] == "LTIM" and int(data["contest_ratings"][i]["rating"]) >= 1800 :
                    short2 += 1
                elif data["contest_ratings"][i]["code"][:4] == "COOK" and int(data["contest_ratings"][i]["rating"]) >= 1800 :
                    short2 += 1
                elif int(data["contest_ratings"][i]["rating"]) >= 1800 :
                    long2 += 1
                else :
                    long1 += 1
                
        # print(short1, long1)
        # print(short2, long2)

        if long1==0 and long2==0:
            same_trend +=1
        elif short1==0 and short2==0:
            same_trend +=1
        elif short1 >= long1:
            if short2 >= long2:
                same_trend +=1
            else:
                opps_trend +=1
        else:
            if short2 < long2:
                same_trend +=1
            else:
                opps_trend +=1

print(same_trend, opps_trend)



