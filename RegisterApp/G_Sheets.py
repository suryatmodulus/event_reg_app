import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/surya43/furore_reg_app/RegisterApp/creds.json', scope)
gc = gspread.authorize(credentials)

def Update_GS(sheet_name,row):
	wks = gc.open(sheet_name).sheet1
	wks.insert_row(row)