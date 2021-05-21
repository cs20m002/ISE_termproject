import json

ratio_up = 0

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
            fully_solved = data["fully_solved"]["count"]
            partially_solved = data["partially_solved"]["count"]
            # print(fully_solved, partially_solved)

            ratio_up += partially_solved / fully_solved

print(ratio_up/1000)

