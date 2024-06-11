


from tkinter import *
from tkinter import ttk
import sqlite3
from DBManager import db
#>>>>>>>>>>>>>>>>> IF YOU SEE TREE VIEW THAT IS THE TABLE

'''
#fake data

data = [
    [1001, "Pehtgncil", 3300, 20],
    [1002, "Penercil", 3002, 20],
    [1003, "Penc434il", 300, 20],
    [1004, "Penrecil", 3200, 20],
    [1005, "Penyucil", 3500, 20]

    ]
'''

#-------------------------------DATABASE STUFF-------------------------------
def create_database():
    #>>>DATABASE CREATION
    
    conn=sqlite3.connect('inventorydb.db')

    #Createacursor instance
    c = conn.cursor()
    
    db.create_table("CustomerTbl","""customerID INTEGER NOT NULL,
        customerFName TEXT NOT NULL,
        customerLName TEXT NOT NULL,
        customerAddress TEXT,
        customerContact	INTEGER,
        PRIMARY KEY("customerID" AUTOINCREMENT)""")

    #Create Customer Table
    c.execute("""CREATE TABLE if not exists CustomerTbl(
        customerID INTEGER NOT NULL,
        customerFName TEXT NOT NULL,
        customerLName TEXT NOT NULL,
        customerAddress TEXT,
        customerContact	INTEGER,
        PRIMARY KEY("customerID" AUTOINCREMENT)
        )
        """)
    
    #Create OrderItem Table
    c.execute("""CREATE TABLE if not exists OrderItemTbl(
        orderID	INTEGER NOT NULL,
        productID	INTEGER NOT NULL,
        quantity	INTEGER NOT NULL,
        salePrice	NUMERIC NOT NULL,
        FOREIGN KEY("orderID") REFERENCES "OrderTbl",
        FOREIGN KEY("productID") REFERENCES "ProductTbl"
        )
        """)
    
    #Create Order Table
    c.execute("""CREATE TABLE if not exists OrderTbl(
        orderID	INTEGER NOT NULL,
        customerID	INTEGER NOT NULL,
        orderDate	TEXT NOT NULL,
        orderTotal	NUMERIC NOT NULL,
        PRIMARY KEY("orderID"),
        FOREIGN KEY("customerID") REFERENCES "CustomerTbl"
        )
        """)
    
    c.execute("""CREATE TABLE if not exists ProductTbl(
        productID	INTEGER NOT NULL,
        productName	TEXT NOT NULL,
        productPrice	NUMERIC DEFAULT 0.0,
        productOnHand	INTEGER DEFAULT 1,
        productDesc	TEXT,
        productAvailability	TEXT NOT NULL DEFAULT 'Available',
        PRIMARY KEY("productID" AUTOINCREMENT)
        )
        """)
        
    

    #Create Table
    c.execute("""CREATE TABLE if not exists Items(
        Item_ID integer Primary Key,
        Item_Name text,
        Quantity integer,
        Price integer
        )
        """)
    
    
    
    '''
    
    --------------------DUMMMY DATAAA AADDD---------------------------
    #add dummy data
    for record in data:
        c.execute("""INSERT or IGNORE INTO Items VALUES(
            
            :Item_ID,
            :Item_Name,
            :Quantity,
            :Price
            
            )""",
            
            {
                'Item_ID': record[0],
                'Item_Name': record[1],
                'Quantity': record[2],
                'Price': record[3],
        
            })
            
    '''
    
    #commit databasee
    conn.commit()

    #close database
    conn.close()
    
    



#---------------------------------------MAIN MENU---------------------------------------



def main_menu():
    global Main
    Main = Tk()
    Main.title("Inventory System")
    
    #>>>Center the main window
    main_width=1000
    main_height=600
    
    screen_width = Main.winfo_screenwidth()
    screen_height = Main.winfo_screenheight() 
    
    x = (screen_width /2) - (main_width/2)
    y = (screen_height /2) - (main_height/1.8)
    
    Main.geometry(f'{main_width}x{main_height}+{int(x)}+{int(y)}')


    create_database()
    

    menu_item()
    
    
    #>>> Code Here
    
    
    
    
    Main.mainloop()
    
    
    
    
#---------------------------------------CUSTOMER---------------------------------------
def menu_customer():
    
    
    print('')
    
    
#---------------------------------------ITEM---------------------------------------
def menu_item():
    
    #Add our data to the screen
    def query_database_items():
        
        #Createadatabase or connect to one that exists
        conn=sqlite3.connect('INVENTORY.db')
        #Createacursor instance
        c = conn.cursor()
        
        c.execute("Select * from Items")
        records = c.fetchall
        
        global count
        count=0


        for record in records():
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values = (record[0], record[1], record[2], record[3]), tags=("evenrow",))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values = (record[0], record[1], record[2], record[3]), tags=("oddrowrow",)) 
            
            #increment counter
            count += 1
    
        
        #commit databasee
        conn.commit()

        #close database
        conn.close()
        


    def add_window_item():
        
        Main.destroy()
        
        add_item = Tk()
        add_item.title("ADD ITEM")
        
        #>>>Center the main window
        add_item_width=500
        add_item_height=500
        
        item_screen_width = add_item.winfo_screenwidth()
        item_screen_height = add_item.winfo_screenheight() 
        
        item_x = (item_screen_width /2) - (add_item_width/2)
        item_y = (item_screen_height /2) - (add_item_height/1.8)
        
        add_item.geometry(f'{add_item_width}x{add_item_height}+{int(item_x)}+{int(item_y)}')

        conn=sqlite3.connect('INVENTORY.db')
        #Createacursor instance
        c = conn.cursor()
        
        c.execute("SELECT MAX(Item_ID) FROM Items")
        item_last = c.fetchall
        
        #Textboxs
    
        data_frame=LabelFrame(add_item, text="Record")
        data_frame.pack(fill="x", expand="yes", padx=20)

        item_id_label=Label(data_frame, text="Item ID")
        item_id_label.grid(row=0, column=0, padx=10, pady=10)
        item_id_entry=Entry(data_frame, text=item_last)
        item_id_entry.grid(row=0, column=1, padx=10, pady=10)
        item_id_entry.config(state='disabled')

        item_name_label=Label(data_frame, text="Item Name")
        item_name_label.grid(row=0, column=3, padx=10, pady=10)
        item_name_entry=Entry(data_frame)
        item_name_entry.grid(row=0, column=4, padx=10, pady=10)  

        quantity_label=Label(data_frame, text="Quantity")
        quantity_label.grid(row=1, column=0, padx=10, pady=10)
        quantity_entry=Entry(data_frame)
        quantity_entry.grid(row=1, column=1, padx=10, pady=10)  

        price_label=Label(data_frame, text="Price")
        price_label.grid(row=1, column=3, padx=10, pady=10)
        price_entry=Entry(data_frame)
        price_entry.grid(row=1, column=4, padx=10, pady=10)
        
        
        add_item.mainloop()

        
        

    
    
    
    
    
    #>>> Item Frame
    Item_frame=Frame(Main, bg='blue',height=560, width=780)
    Item_frame.place(x=200, y=20)
    Item_frame.pack_propagate(0)
    
    
    #>>>Add Some Style
    style=ttk.Style()

    #>>>PickATheme
    style.theme_use('default')


    #>>>Configure the Treeview Colors
    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")
    
    #>>>Change Selected Color
    style.map('Treeview',
    background = [('selected', "#347083")])

    #>>>Create a Treeview Frame Here you can edit the size of the table
    tree_frame=Frame(Item_frame, height=300, width=500)
    tree_frame.pack(pady=20)
    tree_frame.pack_propagate(0)

    #>>>Create a Treeview Scrollbar
    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)

    #>>>Create The Treeview
    my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #>>>Configure the Scrollbar
    tree_scroll.config(command = my_tree.yview)

    #>>>Define Our Columns
    my_tree['columns']=("Item_ID", "Item_Name", "Quantity","Price")


    #Format Our Columns
    my_tree.column ("#0", width=0, stretch=NO)
    my_tree.column("Item_ID", anchor=CENTER, width=140)
    my_tree.column ("Item_Name", anchor=CENTER, width=140)
    my_tree.column ("Quantity", anchor=CENTER, width=100)
    my_tree.column ("Price", anchor=CENTER, width=140)

    #Format HEadings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Item_ID", text="Item_ID", anchor=CENTER)
    my_tree.heading("Item_Name", text="Item_Name", anchor=CENTER)
    my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
    my_tree.heading("Price", text="Price", anchor=CENTER)
    

    #Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")


    
        
    #>>>>>>>>>>>>>>>>FUCTION>>>>>>>>>>>>>>>>>>>>>
    #Select Record
    def select_record_item(e):
        #Clear entry boxes
        item_id_entry.delete(0, END)
        item_name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
    
        #Grab record Number
        selected=my_tree.focus()
    
        #Grab record values
        values = my_tree.item(selected, 'values')

        item_id_entry.insert(0, values[0])
        item_name_entry.insert(0, values[1])
        quantity_entry.insert(0, values[2])
        price_entry.insert(0, values[3])
        
    #clear entry
    def clear_entry_item():
        item_id_entry.delete(0, END)
        item_name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)

    
    def add_record_item():
        
        #Createadatabase or connect to one that exists
        conn=sqlite3.connect('INVENTORY.db')

        #Createacursor instance
        c=conn.cursor()
        
        c.execute("""INSERT INTO Items VALUES(
            
            :Item_ID,
            :Item_Name,
            :Quantity,
            :Price
            
            )""",
            
            {
                'Item_ID': item_id_entry.get(),
                'Item_Name': item_id_entry.get(),
                'Quantity': quantity_entry.get(),
                'Price': price_entry.get(),
        
            })
        
        #commit databasee
        conn.commit()

        #close database
        conn.close()
        
        #Clear entry boxes
        item_id_entry.delete(0, END)
        item_name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        
        #Clear The Treeview Table
        my_tree.delete(*my_tree.get_children())
        
        query_database_items()
        
    
    def update_record_item():
        
        #Grab the record number
        selected=my_tree.focus()
        #Update record
        my_tree.item(selected, text="", values=(item_id_entry.get(), item_name_entry.get(), quantity_entry.get(), price_entry.get(),))

        #Clear entry boxes
        item_id_entry.delete(0, END)
        item_name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        
        #Createadatabase or connect to one that exists
        conn=sqlite3.connect('INVENTORY.db')

        #Createacursor instance
        c=conn.cursor()

        conn.execute("""UPDATE Items SET
            Item_Name=:item_name,
            Quantity=:quantity,
            Price=:price,
        
            WHERE Item_ID=:item_id""",
            {
                'Item_Name': item_id_entry.get(),
                'Quantity': quantity_entry.get(),
                'Price': price_entry.get(),
                'Item_ID': item_id_entry.get(),
                
            })

        #commit databasee
        conn.commit()

        #close database
        conn.close()
    
    #>>>>>>>>>>>>>END OF FUNCTIOM>>>>>>>>>>>>>
       
    #Textboxs
    
    data_frame=LabelFrame(Item_frame, text="Record")
    data_frame.pack(fill="x", expand="yes", padx=20)

    item_id_label=Label(data_frame, text="Item ID")
    item_id_label.grid(row=0, column=0, padx=10, pady=10)
    item_id_entry=Entry(data_frame)
    item_id_entry.grid(row=0, column=1, padx=10, pady=10)

    item_name_label=Label(data_frame, text="Item Name")
    item_name_label.grid(row=0, column=3, padx=10, pady=10)
    item_name_entry=Entry(data_frame)
    item_name_entry.grid(row=0, column=4, padx=10, pady=10)  

    quantity_label=Label(data_frame, text="Quantity")
    quantity_label.grid(row=1, column=0, padx=10, pady=10)
    quantity_entry=Entry(data_frame)
    quantity_entry.grid(row=1, column=1, padx=10, pady=10)  

    price_label=Label(data_frame, text="Price")
    price_label.grid(row=1, column=3, padx=10, pady=10)
    price_entry=Entry(data_frame)
    price_entry.grid(row=1, column=4, padx=10, pady=10)
    
    
    #Add Buttons
    button_frame= LabelFrame(Item_frame, text="Commands")
    button_frame.pack(fill="x", expand="yes", padx=20) 

    add_button=Button(button_frame, text="Add Record", command=add_window_item)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button=Button(button_frame, text="Update Record", command=update_record_item)
    update_button.grid(row=0, column=2, padx=10, pady=10)

    del_button=Button(button_frame, text="Delete Record")
    del_button.grid(row=0, column=3, padx=10, pady=10)

    clear_button=Button(button_frame, text="Clear Entry", command=clear_entry_item)
    clear_button.grid(row=0, column=4, padx=10, pady=10)

    search_button=Button(button_frame, text="Search Record")
    search_button.grid(row=0, column=5, padx=10, pady=10)

    #if the table is click the information will pe pass on textbox
    my_tree.bind("<ButtonRelease-1>", select_record_item)
    
    #>>> Refresh or load the data on table
    query_database_items()
                

    
        
    
    
main_menu()
    
    
    

    

