#!/usr/bin/python3
#
# Usage: test-sheet.py 
# 

import sys
import re
import csv

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

def main():
  json_key = json.load(open("google/nba-players-3a8894677b14.json"))
  scope = ['https://spreadsheets.google.com/feeds']
  credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open("lista igraca").sheet1
  with open("players.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(worksheet.get_all_values())

  worksheet = gc.open("lista igraca").get_worksheet(3)
  with open("games.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(worksheet.get_all_values())

if __name__ == '__main__':
  main()