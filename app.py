import datetime

from flask import Flask, abort, jsonify, request

from inspector import Inspector

app = Flask(__name__)


@app.route("/search", methods=["GET"])
def search():
    myData = [] # store the filtered data
    
    allData = Inspector.get_inspections()   # get all the data

    # If no restaurant_name is given then its None by defult
    if "restaurant_name" in request.args:
        restaurant_name = request.args.get("restaurant_name") # get the restaurant name provided in the URL
    else:
        restaurant_name = "None"
    # If no cusine then its None by defult
    if "cusine" in request.args:
        cusine = request.args.get("cusine") # get the cusine if given in the params
    else:
        cusine = "None"
    # If no zipcode then its None by defult
    if "zipcode" in request.args:
        zipcode = request.args.get("zipcode") # get the zipcode number if given in the params
    else:
        zipcode = "None"

    limit = 10 # limit is 10 by defult 
    # Check for limit if given
    if "limit" in request.args:
        limit = int(request.args.get("limit"))
  
    # loop through the data to filter
    for data in allData:
        # break of loop when limit get to 0
        if limit == 0:
            break
        # Apply the filters. 
        # Check if params have value and if that same value is in the avaliable in the data
        # appened that value with its data to the filtered list
        # CaseFold() method: used to check for case insensitive
        if restaurant_name == 'None' or restaurant_name.casefold() in data.restaurant_name.casefold():
            if cusine == 'None' or cusine.casefold() in data.cusine.casefold():
                if zipcode == 'None' or zipcode in data.zipcode:
                    myData.append(data.to_json())#
                    limit -= 1 # decrement limit by 1 each time we append

    # resturn the list with the filtered data
    return jsonify({"data": myData})

if __name__ == "__main__":
    app.run(debug=True)
