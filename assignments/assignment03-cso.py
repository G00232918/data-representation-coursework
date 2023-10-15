# Student name: James Connolly
# Student no: G00232918
# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json"
# References -
# data webpage - https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series/resource/24833b36-fede-4e00-bf8d-f08c3e2abf10
# reference to create program - https://realpython.com/python-json/#a-real-world-example-sort-of
# if statement example - https://www.geeksforgeeks.org/response-json-python-requests/

# Import required libraries
import requests
import json

# Define the URL for the dataset
URL = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Get the response from the URL
response = requests.get(URL)

# Check if the reponse URL is available
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    # open the the json in the write format
    with open("cso_ex_hist.json", "w") as f:
        # Write the JSON data to the file
        json.dump(data, f)
    # Print a success message
    print("Dataset saved as cso_ex_hist.json")
else:
    # Print an error message
    print("The request failed", response.status_code)