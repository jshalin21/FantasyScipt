import gspread
from sleeperpy import Leagues,Players,Drafts,User
import time
from tkinter import *

root = Tk()

root.title("Fantasy Football App")
root.configure(background="navy")
root.geometry('350x200')
root.mainloop()

def draftScript():
    account = User.get_user('sjoshi2004') #Username

    sa = gspread.service_account(filename="service_account.json")
    sheet = sa.open("Fantasy Rankings")

    wks1 = sheet.worksheet("Fantasy Pros PPR")
    wks2 = sheet.worksheet("LOEBS Leads PPR")
    wks3 = sheet.worksheet("NO BS PPR")

    pick = 0
    userPick = 3

    while pick < 150:
        draft = Drafts.get_all_picks_in_draft(997031959723298816) #replace with draft ID
        
        if pick < len(draft):
            pick_info = draft[pick]
            pick_no = pick_info['pick_no']
            
            if pick == pick_no - 1:
                firstName = pick_info['metadata']['first_name']
                lastName = pick_info['metadata']['last_name']
                Name = firstName + " " + lastName

                cell1 = wks1.find(Name)

                if cell1 is None:
                    print("Player Not Found: ", Name)
                else:
                    row = str(cell1.row)
                    col = str(cell1.col)
                    location = "A" + row + ":" + "F" + row
                    wks1.format(location, {"backgroundColor": {"red": 25}})
                    print("Player drafted:", Name)

                cell2 = wks2.find(Name)

                if cell2 is None:
                    print("Player Not Found: ", Name)
                else:
                    row2 = str(cell2.row)
                    col2 = str(cell2.col)
                    location2 = "A" + row2 + ":" + "E" + row2
                    wks2.format(location2, {"backgroundColor": {"red": 25}})
                    #print("Player drafted:", Name)

                cell3 = wks3.find(Name)

                if cell3 is None:
                    print("Player Not Found: ", Name)
                else:
                    row3 = str(cell3.row)
                    col3 = str(cell3.col)
                    location3 = "A" + row3 + ":" + "F" + row3
                    wks3.format(location3, {"backgroundColor": {"red": 25}})
                    #print("Player drafted:", Name)
                
                pick += 1

        # Wait for a period of time before checking again (e.g., every 10 seconds)
        time.sleep(0.5)

