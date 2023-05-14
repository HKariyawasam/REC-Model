import pandas as pd
from openpyxl import load_workbook
import requests


# Define the shared link URL of the Google Sheets document
shared_link_url1 = "https://docs.google.com/spreadsheets/d/10AQCTZt-mpp0xQ5T4UnU0-yLNCZ-OPr3/export?format=xlsx"
shared_link_url2 = "https://docs.google.com/spreadsheets/d/1j-xZhA0ozhsDRXf-0qoAqrGgHxF-dwpo/export?format=xlsx"
shared_link_url3 = "https://docs.google.com/spreadsheets/d/1j-xZhA0ozhsDRXf-0qoAqrGgHxF-dwpo/export?format=xlsx"
# Send a GET request to download the CSV data
response1 = requests.get(shared_link_url1)
response2 = requests.get(shared_link_url2)
response3 = requests.get(shared_link_url3)

def readActivityDataFrame():
    # activities_df = pd.read_excel(spreadsheet_url1)
    if response1.status_code == 200:
        buffer1 = response1.content
        activities_df = pd.read_excel(buffer1, engine="openpyxl")
        return activities_df

def readUsersCompletionDataFrame():
    # completerates_df = pd.read_excel(spreadsheet_url2)
    if response2.status_code == 200:
        buffer2 = response2.content
        completerates_df = pd.read_excel(buffer2, engine="openpyxl")
        return completerates_df 

def updateUserCompletionRates(data):
    userId = int(data['userId'])
    activityId = int(data['activityId'])
    complete_score = int(data['complete_score'])
    satisfaction_score = float(data['satisfaction_score'])

    if response3.status_code == 200:
        buffer3 = response3.content
        book = pd.read_excel(buffer3, engine="openpyxl")

    wb_append = load_workbook(shared_link_url3)

    sheet = wb_append.active
    row = (userId,activityId, complete_score,satisfaction_score)
    sheet.append(row)
    wb_append.save(shared_link_url3)