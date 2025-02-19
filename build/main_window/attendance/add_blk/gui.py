
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def addBlk():
    AddBlk()
    

class AddBlk(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.data = {"blk": StringVar(), "no_students": StringVar(),"no_present": StringVar(),"no_absent": StringVar(),"no_late": StringVar()} 
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 622,
            width = 983,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            983.0,
            622.0,
            fill="#FFFFFF",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            76.0,
            219.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            169.0302734375,
            257.0,
            image=self.image_image_2
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            169.56288146972656,
            242.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            textvariable=self.data["blk"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=52.0302734375,
            y=230.0,
            width=235.06521606445312,
            height=23.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            169.0302734375,
            343.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            128.0,
            305.0,
            image=self.image_image_4
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            169.56288146972656,
            328.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            textvariable=self.data["no_students"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=52.0302734375,
            y=316.0,
            width=235.06521606445312,
            height=23.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            relief="flat"
        )
        button_1.place(
            x=100.34405517578125,
            y=378.0,
            width=114.28071594238281,
            height=38.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            632.7939453125,
            351.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            490.9442138671875,
            61.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            490.3062744140625,
            61.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            731.0,
            62.0,
            image=self.image_image_8
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("up"),
            relief="flat"
        )
        button_2.place(
            x=54.2088623046875,
            y=45.0,
            width=456.1937561035156,
            height=35.0
        )
   
    def save(self):

        self.data["no_present"].set("0")
        self.data["no_absent"].set("0")
        self.data["no_late"].set("0")
        for val in self.data.values():
            if val.get() == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return

     
        result = db_controller.add_section(
            *[self.data[label].get() for label in ("blk", "no_students", "no_present","no_absent","no_late")]
        )

        if result:
            messagebox.showinfo("Success", "section added successfully")
            self.parent.windows.get("up").handle_refresh()
            for label in self.data.keys():
                self.data[label].set('')
        else:
            messagebox.showerror(
                "Error", "Unable to add section. Please make sure the data is validated"
            )
      
