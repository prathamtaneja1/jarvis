                                                                                    #School Project#
                                                                                  #file data handling#
import pickle



def add_data():
    emp=[ ]                                                                           
    f=open("hotel.dat","rb+")                                                  
    ans='y'

    
    while ans=='y':                                                                       
        room=int(input("Enter room number:"))
        name=input("Enter your name:")
        days=int(input("Enter how many days you want to spend:"))
               
        emp.append([room,name,days])                                                             
        ans=input("Want to enter more records-press 'y':")
    pickle.dump(emp,f)                                                                                       
    f.close()






# MODIFY DATA

def modify_data():
    emp=[]
    f=open("hotel.dat","rb")
    emp=pickle.load(f)
    print("Contents before modification\n",emp)
    e=int(input("\n enter the room no. you want to modify:"))
    found=0
    for d in emp:
        if d[0]==e:
            d[2]=d[2]+1000
            found=1
            break
    if found==0:
        print("record not found")
    f.close()


emp=[]
f=open("hotel.dat","wb")
pickle.dump(emp,f)
f.close()


#DELETE DATA

def delete_data():
    f=open("hotel.dat","rb")
    emp=[]
    emp=pickle.load(f)
    f.close()
    print("content before deletion",emp)

    f=open("hotel.dat","wb")
    e=int(input("enter room no. you want to delete:"))
    l=[]
    found=0
    for d in emp:
        if d[0]!=e:
            l.append(d)
        else:
            found=1
    if found==0:
        print("record not found")


    pickle.dump(l,f)
    f.close()
            





#DISPLAY EMPLOYEE DATA

def display_data():

    import pickle
    emp=[]
    f=open("hotel.dat","rb")
    emp=pickle.load(f) 

    for d in emp:
        print(d)
    f.close()






#SEARCH EMPLOYEE DATA

def search():
    emp=[]
    f=open("hotel.dat","rb")
    e=int(input("Enter room no you want to search:"))

    emp=pickle.load(f)
    found=0
    for d in emp:
        if d[0]==e:
            found=1
            print("Room found:",d)
            break

    if found==0:
        print("record not found")
    f.close()



# MAIN MENU

ch=0
while ch!=6:
    print('\n'*30)
    print("##.....HOTEL MANAGEMENT.....##  \n                 Welcome \n         How can I help you!")
    print("1. Add new room Details")
    print("2. Modify hotel data")
    print("3. Delete hotel data")
    print("4. Display")
    print("5. Search an hotel data")
    print("6. Exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        print('\n'*20)
        add_data()
        a=input("Press any key to go back to main menu")

    elif ch==2:
        print('\n'*20)
        modify_data()
        a=input("Press any key to go back to main menu")

    elif ch==3:
        print('\n'*20)
        delete_data()
        a=input("Press any key to go back to main menu")

    elif ch==4:
        print('\n'*20)
        display_data()
        print('\n'*4)
        a=input("Press any key to go back to main menu")


    elif ch==5:
        print('\n'*20)
        search()
        a=input("Press any key to go back to main menu")


    elif ch==6:
        break

    else:
        print("Enter a number between 1 to 6 only......")
        a=input("Press any key to go back to main menu")


        
                                                                                             #By Vishesh and Nikhil Rathore





    
