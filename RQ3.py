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
            pass
            # still work left



