
        #using datbases
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


root=Tk()
root.title("DATABASES OF STUDENT")
root.iconbitmap("ico.ico")
root.geometry("350x400")


#create a database or connect to datbase
conn=sqlite3.connect('adres_book.db')


#creating a cursor
c=conn.cursor()
#create table
'''c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")'''

#update function
def update():
    #create a database or connect to datbase
    conn=sqlite3.connect('adres_book.db')


    #creating a cursor
    c=conn.cursor()
    
    record_id=deletes.get()
    
    c.execute("""UPDATE addresses SET
            first_name=:first,
            last_name=:last,
            address=:address,
            city=:city,
            state=:state,
            zipcode=:zipcode

            WHERE oid=:oid""",
            {'first':f_name_editor.get(),
             'last':last_name_editor.get(),
             'address':address_editor.get(),
             'city':city_editor.get(),
             'state':state_editor.get(),
             'zipcode':zipcode_editor.get(),

             'oid':record_id
             })
    
    #connection changes
    conn.commit()

    #conection close  
    conn.close()

    editor.destroy()

    '''f_name_editor.delete(0,END)
    last_name_editor.delete(0,END)
    address_editor.delete(0,END)
    city_editor.delete(0,END)
    state_editor.delete(0,END)
    zipcode_editor.delete(0,END)'''




#edit function
def edit():
    global editor
    
    editor=Tk()
    editor.title("DATBASES OF STUDENT")
    editor.geometry("300x215")
    editor.iconbitmap("ico.ico")
    #create a database or connect to datbase
    conn=sqlite3.connect('adres_book.db')


    #creating a cursor
    c=conn.cursor()

    record_id=deletes.get()
    #Query the datbase
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records=c.fetchall()

    #making testbox names global to access in update function
    global f_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    


    #create test box 
    f_name_editor=Entry(editor,width=30,bd=5)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(5,0))

    last_name_editor=Entry(editor,width=30,bd=5)

    last_name_editor.grid(row=1,column=1,padx=20)

    address_editor=Entry(editor,width=30,bd=5)
    address_editor.grid(row=2,column=1,padx=20)

    city_editor=Entry(editor,width=30,bd=5)
    city_editor.grid(row=3,column=1,padx=20)

    state_editor=Entry(editor,width=30,bd=5)
    state_editor.grid(row=4,column=1,padx=20)

    zipcode_editor=Entry(editor,width=30,bd=5)
    zipcode_editor.grid(row=5,column=1,padx=20)


    #creating box labels
    f_label=Label(editor,text="First Name").grid(row=0,column=0)
    l_label=Label(editor,text="Last Name").grid(row=1,column=0)
    a_label=Label(editor,text="address Name").grid(row=2,column=0)
    c_label=Label(editor,text="city Name").grid(row=3,column=0)
    s_label=Label(editor,text="state Name").grid(row=4,column=0)
    z_label=Label(editor,text="zipcode").grid(row=5,column=0)
    #d_label_editor=Label(editor,text="enter primary key to be deleted:").grid(row=7,column=1,padx=(30,0),pady=3)

    bu=Button(editor,text="update data to the datbase",command=update).grid(row=6,column=0,columnspan=3,pady=10,ipadx=60,ipady=3)

    for record in records:
        f_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    
    
    #connection changes

    conn.commit()

    #conection close

    conn.close()
        
#function to exit
def nooo():
    r=messagebox.showerror("DATABASE APP","Are you sure to exit this page")
    if r=="ok":
        return
#function to display the elemnts in new page
def avenger():
    s=messagebox.askyesno("database program","Are you sure you want to display new page")
    if s==1:
        top=Toplevel()
        top.geometry("720x720")
        #create a database or connect to datbase
        conn=sqlite3.connect('adres_book.db')



        #creating a cursor
        c=conn.cursor()

        #query  database
        c.execute("SELECT *,oid FROM addresses")
        records=c.fetchall()
        print_records=''

        
        for record in  records:
            print_records+=str(record[0])+" "+str(record[1])+"\t"+str(record[6])+"\n"
        query_label=Label(top,text=print_records).grid(row=1,column=0,pady=10,ipady=3)
        qui=Button(top,text="HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME HOME",fg="red",command=top.destroy).grid(row=0,column=0,columnspan=3,pady=10,ipadx=100,ipady=7)


        #commit changes
        conn.commit()

        #close connection
        conn.close()
    else:
        return
#delete a record
def delete():
    #create a database or connect to datbase
    conn=sqlite3.connect('adres_book.db')

   
    #creating a cursor
    c=conn.cursor()

   


    #query  database
    c.execute("DELETE from addresses WHERE oid="+deletes.get())

    

    
    
    
    

    #commit changes
    conn.commit()

    #close connection
    conn.close()
#clear function
#def clear():
    


#creating submit function
def submit():
    #create a database or connect to datbase
    conn=sqlite3.connect('adres_book.db')


    #creating a cursor
    c=conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name,:last_name,:address,:city,:state,:zipcode)",
    {
                    'f_name':f_name.get(),
                    'last_name':last_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get(),
    })


    #commit changes
    conn.commit()

    #close connectio
    conn.close()

    f_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#query function
def query():
    #create a database or connect to datbase
    conn=sqlite3.connect('adres_book.db')



    #creating a cursor
    c=conn.cursor()

    #query  database
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print_records=''

    #looping through results
    #top=Toplevel()
    #top.geometry("400x400")
    #clear button
    #clear=Button(top,text="clear data",fg="red",command=top.destroy).grid(row=0,column=0,padx=10,pady=20,columnspan=3,ipadx=150)

    for record in  records:
        print_records+=str(record[0])+" "+str(record[1])+"\t"+str(record[6])+"\n"
    #query_label=Label(top,text=print_records).grid(row=2,column=0,columnspan=2)
    query_label=Label(root,text=print_records).grid(row=9,column=0,columnspan=2)



    #commit changes
    conn.commit()

    #close connection
    conn.close()

    
#create test box 
f_name=Entry(root,width=30,bd=5)
f_name.grid(row=0,column=1,padx=20,pady=(5,0))

last_name=Entry(root,width=30,bd=5)
last_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30,bd=5)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30,bd=5)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30,bd=5)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30,bd=5)
zipcode.grid(row=5,column=1,padx=20)

deletes=Entry(root,text="enter the id no:",width=10,bd=5)
deletes.grid(row=7,column=1,padx=(0,210))

#creating box labels
f_label=Label(root,text="First Name").grid(row=0,column=0)
l_label=Label(root,text="Last Name").grid(row=1,column=0)
a_label=Label(root,text="address Name").grid(row=2,column=0)
c_label=Label(root,text="city Name").grid(row=3,column=0)
s_label=Label(root,text="state Name").grid(row=4,column=0)
z_label=Label(root,text="zipcode").grid(row=5,column=0)
d_label=Label(root,text="enter primary key to be deleted:").grid(row=7,column=1,padx=(30,0),pady=3)




#creating a submit button

b=Button(root,text="upload  to datbase",command=submit).grid(row=6,column=1,columnspan=2,padx=(0,5),pady=(5,0),ipadx=50)

#creating edit button
be=Button(root,text="edit database",command=edit).grid(row=6,column=0,columnspan=2,padx=(0,200),pady=(5,0))


          
#create a query button

bq=Button(root,text="show recorded data",command=query).grid(row=8,column=0,columnspan=2,padx=(0,150),pady=(0,2),ipadx=40)

#create a delete button

bd=Button(root,text="delete record",command=delete).grid(row=7,column=0,padx=(20,1),pady=(8,8),ipady=1)

#destroy button

bd=Button(root,text="EXIT!",fg="red",command=root.destroy).grid(row=8,column=1,padx=(106,0),ipadx=30)

#new item
my_image=ImageTk.PhotoImage(Image.open("C:/Users/saite/Downloads/avengers-png-logo-4973.png"))
#print(

bd=Button(root,image=my_image,command=avenger).grid(row=8,column=1,padx=(0,23),ipadx=5,ipady=2)

#connection changes

conn.commit()

#conection close

conn.close()


root.mainloop()
