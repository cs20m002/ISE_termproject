import json

long_short_count = []

for i in range(0,1000):
    json_file = "user"+str(i+1)+".json"
    with open(json_file) as f:
        data = json.load(f)
        # print(json_file + " : " + str(len(data["contest_ratings"])))

        keyErrorHandling1 = data.get("message")
        keyErrorHandling2 = data.get("status")

        if keyErrorHandling1 == "Internal Server Error" :
            long_short_count.append([0,0])
        elif keyErrorHandling2 == "Failed":
            long_short_count.append([0,0])
        else :
            long = 0
            short = 0
            for i in range(0,len(data["contest_ratings"])):
                # print(data["contest_ratings"][i]["code"][:4])
                if data["contest_ratings"][i]["code"][:4] == "COOK":
                    short += 1
                elif data["contest_ratings"][i]["code"][:4] == "LTIM":
                    short += 1
                else :
                    long += 1
                
            users = []
            # data cleansing
            if long + short == len(data["contest_ratings"]) :
                users.append(long)
                users.append(short)
                long_short_count.append(users)
            else :
                users.append(0)
                users.append(0)
                long_short_count.append(users)
        
# for i in range (0, len(long_short_count)):
#     print(long_short_count[i])

import xlsxwriter

workbook = xlsxwriter.Workbook('long_short_count.xlsx')
worksheet = workbook.add_worksheet()

col = 0

for row , data in enumerate(long_short_count):
    # print(data, row)
    worksheet.write_row(row , col , data)

workbook.close() 

