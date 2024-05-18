
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Style, Treeview
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def updateAttendance():
    UpdateAttendance()
    
    
class UpdateAttendance(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid   
        self.search_query = StringVar()
        
        self.data = {
            "id": StringVar(),
            "blk": StringVar(),
            "no_students": StringVar(),
            "no_present": StringVar(),
            "no_absent": StringVar(),
            "no_late": StringVar(),
        }



        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 622,
            width = 983,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            983.0,
            622.0,
            fill="#FFFFFF",
            outline="")
        
          
        self.id_text =self.canvas.create_text(
            111.0,
            470.0,
            anchor="nw",
            text="01",
            fill="#FFFFFF",
            font=("Montserrat SemiBold", 17 * -1)
        )
        
        

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            490.9442138671875,
            61.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            490.30621337890625,
            61.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            257.7969970703125,
            61.0,
            image=self.image_image_3
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("add"),
            relief="flat"
        )
        button_1.place(
            x=482.2088928222656,
            y=44.0,
            width=456.1937561035156,
            height=35.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            833.0,
            164.0,
            image=self.image_image_4
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            838.9876937866211,
            164.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.search_query
        )
        
        entry_1.bind(
            "<KeyRelease>",
            lambda event: self.filter_treeview_records(self.search_query.get()),
        )
        entry_1.place(
            x=752.580322265625,
            y=152.0,
            width=172.8147430419922,
            height=22.0
        )

        self.canvas.create_text(
            754.0,
            152.0,
            anchor="nw",
            text="Search...",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.edit_btn = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_edit,
            relief="flat"
        )
        self.edit_btn.place(
            x=603.0,
            y=550.0,
            width=145.87051391601562,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.initialize,
            relief="flat"
        )
        button_3.place(
            x=440.0,
            y=550.0,
            width=145.87051391601562,
            height=48.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.delete_btn = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_delete,
            relief="flat"
        )
        self.delete_btn.place(
            x=761.0,
            y=550.0,
            width=176.53118896484375,
            height=48.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_update,
            relief="flat"
        )
        button_5.place(
            x=78.9744873046875,
            y=475.0,
            width=123.57183074951172,
            height=38.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            159.7391357421875,
            369.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            94.5,
            331.0,
            image=self.image_image_6
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            160.27174377441406,
            354.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            textvariable=self.data["no_absent"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=42.7391357421875,
            y=342.0,
            width=235.06521606445312,
            height=23.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            159.7391357421875,
            292.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            94.5,
            254.0,
            image=self.image_image_8
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            160.27174377441406,
            277.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            self,
            textvariable=self.data["no_present"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=42.7391357421875,
            y=265.0,
            width=235.06521606445312,
            height=23.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = self.canvas.create_image(
            67.0,
            179.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        image_10 = self.canvas.create_image(
            159.7391357421875,
            217.0,
            image=self.image_image_10
        )

        self.block_text = self.canvas.create_text(
            43.0,
            195.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("MontserratRoman Regular", 12 * -1)
        )

 

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        image_11 = self.canvas.create_image(
            734.344970703125,
            164.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        image_12 = self.canvas.create_image(
            55.9442138671875,
            574.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        image_13 = self.canvas.create_image(
            159.7391357421875,
            454.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        image_14 = self.canvas.create_image(
            81.5,
            416.0,
            image=self.image_image_14
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            160.27174377441406,
            439.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            self,
            textvariable=self.data["no_late"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=42.7391357421875,
            y=427.0,
            width=235.06521606445312,
            height=23.0
        )
        
        self.canvas.create_rectangle(
            354.92059326171875,
            195.0,
            955.1266479492188,
            539.0,
            fill="#D9D9D9",
            outline="")
     
        self.columns = {
            "ID": ["ID", 10],
            "blk": ["Block", 40],
            "no_students": ["No. of Students", 40],
            "no_present": ["No. of Present", 40],
            "no_absent": ["No. of Absent", 40],
            "no_late": ["No. of Late", 40],
        }
        
                # Create a style
        self.style = Style(self)
        self.style.configure("Custom.Treeview", background="#FFFFFF")
        self.style.map("Custom.Treeview",
                       background=[("selected", "#117EE4")])

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            style="Custom.Treeview"
            # bg="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0],anchor='center')
            self.treeview.column(idx, width=txt[1],anchor='center')

        self.treeview.place(x=354.92059326171875, y=195, width=600.21, height=344)
  
        self.handle_refresh()   

        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

    def filter_treeview_records(self, query):
        self.treeview.delete(*self.treeview.get_children())
    
        for row in self.block_data:
           
            if query.lower() in str(row).lower():
            
                self.treeview.insert("", "end", values=row)
        self.on_treeview_select()

    def on_treeview_select(self, event=None):
        try:
            self.treeview.selection()[0]
        except IndexError:
            self.parent.selected_rid = None
            return
   
        item = self.treeview.selection()[0]
      
        self.parent.selected_rid = self.treeview.item(item, "values")[0]
    
        self.delete_btn.config(state="normal")
        self.edit_btn.config(state="normal")

    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.block_data = db_controller.get_section()
        print("self blk data: ", self.block_data)
        for row in self.block_data:
            self.treeview.insert("", "end", values=row)

     #def handle_navigate_back(self):
        #self.parent.navigate("add")

    def handle_delete(self):
        if db_controller.delete_section(self.parent.selected_rid):
            messagebox.showinfo("Success","Successfully Deleted the table")
        else:
            messagebox.showerror("failed","Unable to delete table")

        self.handle_refresh()

    def initialize(self):
            self.block_data = db_controller.get_section()
            self.selected_r_id = self.parent.selected_rid
    
            if self.block_data is not None:
                self.selected_block_data = list(
                    filter(lambda x: str(x[0]) == self.selected_r_id, self.block_data)
                )

                if self.selected_block_data:
                    self.selected_block_data = self.selected_block_data[0]

                    self.canvas.itemconfigure(self.id_text, text=self.selected_block_data[0])
                    self.canvas.itemconfigure(self.block_text, text=self.selected_block_data[1])
                 


                    
    def handle_update(self):
        result = db_controller.update_section(
            self.selected_r_id,
            no_present=self.data["no_present"].get(),
            no_absent=self.data["no_absent"].get(),
            no_late=self.data["no_late"].get(),       
        )
    
        if result:
            messagebox.showinfo("Success", "Details updated successfully")
            self.handle_refresh()
            for label in self.data.keys():
                self.data[label].set("")
        else:
            messagebox.showerror("Error", "Failed to update details")
            
    def handle_edit(self):
        self.parent.navigate("all")
        self.parent.windows["all"].initialize2()
        self.handle_refresh()