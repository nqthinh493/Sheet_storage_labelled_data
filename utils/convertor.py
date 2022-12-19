import csv 
import json
import time
import requests

def convert_csv_to_json(csvFilePath, jsonFilePath):
    print('Convert CSV --> JSON file......')
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def add_data_to_json(jsonTempFilePath,jsonFilePath):
    with open(jsonFilePath, "r") as jsonFile:
        try:
            data = json.load(jsonFile)
        except:
            data = []
    with open(jsonTempFilePath, "r") as tempFile:
        tempLabelledData = json.load(tempFile)
    data.extend(tempLabelledData)
    with open(jsonFilePath, "w") as file:
        json.dump(data, file, indent=4)

def convert_sheet_to_json(url, jsonFilePath):
    print('Converting DATASHEET ---> JSON file......')
    data = requests.get(url).text
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_file.write(data)

    with open(jsonFilePath) as json_file:
        data1 = json.load(json_file)
    
# csvFilePath = r'D:/Downloads/via_infant_test.csv'
# jsonFilePath = r'./current.json'
# jsonTempFilePath =r'./temp.json'
# start = time.perf_counter()
# convert_csv_to_json(csvFilePath, jsonTempFilePath)
# add_data_to_json(jsonTempFilePath, jsonFilePath)
# finish = time.perf_counter()

# print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")