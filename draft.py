import gspread
from sleeperpy import Leagues,Players,Drafts,User
import time
import tkinter as tk



def draftGui():
    root = tk.Tk()
    root.title("Draft Helper")
    #root.configure(background="navy")
    root.geometry('350x200')
    
    usr_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    usr_entry = tk.Entry(root, font=('calibre',10,'normal'))
    
    id_label = tk.Label(root, text = 'Draft ID', font = ('calibre',10,'bold'))
    id_entry=tk.Entry(root, font = ('calibre',10,'normal'))
    
    def submit():
        usrname = usr_entry.get()
        id = id_entry.get()
        draftScript(int(id),usrname)
        print("Username: ", usrname)
        print("id: ", id)
    
    sub_btn=tk.Button(root,text = 'Start', command = submit)


    usr_label.grid(row=0,column=0)
    usr_entry.grid(row=0,column=1)
    id_label.grid(row=1,column=0)
    id_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)


    

def draftScript(draftID, username="sjoshi2004"):
    account = User.get_user(username) #Username

    sa = gspread.service_account(filename="service_account.json")
    sheet = sa.open("Fantasy Rankings")

    wks1 = sheet.worksheet("Fantasy Pros PPR")
    wks3 = sheet.worksheet("NO BS PPR")

    pick = 0
    userPick = 3
    print(type(draftID))
    print(draftID)
    while pick < 150:
        #997031959723298816
        draft = Drafts.get_all_picks_in_draft(draftID) #replace with draft ID
        
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
        time.sleep(0.8)

if __name__ == "__main__":
    print("This is a different version of the module.py file.")