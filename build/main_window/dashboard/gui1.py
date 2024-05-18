from pathlib import Path
from tkinter import Frame, Tk, Canvas, Button, PhotoImage
import controller as db_controller
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Dashboard(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=622,
            width=983,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            983.0,
            622.0,
            fill="#F8F6F6",
            outline=""
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(490.94422912597656, 61.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.canvas.create_image(490.3062438964844, 61.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.canvas.create_image(490.8270263671875, 61.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.canvas.create_image(788.1654052734375, 215.0, image=self.image_image_4)

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.canvas.create_image(170.30624389648438, 217.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.canvas.create_image(170.30624389648438, 406.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.canvas.create_image(479.70037841796875, 217.0, image=self.image_image_8)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    

        self.total_present = self.canvas.create_text(
            135.0,
            212.0,
            anchor="nw",
            text="400",
            fill="#000000",
            font=("MontserratRoman Bold", 36 * -1)
        )

        self.total_late = self.canvas.create_text(
            137.0,
            392.0,
            anchor="nw",
            text="400",
            fill="#000000",
            font=("MontserratRoman Bold", 36 * -1)
        )

        self.total_student = self.canvas.create_text(
            446.0,
            212.0,
            anchor="nw",
            text="400",
            fill="#000000",
            font=("MontserratRoman Bold", 36 * -1)
        )

        self.total_absent = self.canvas.create_text(
            755.0,
            212.0,
            anchor="nw",
            text="400",
            fill="#000000",
            font=("MontserratRoman Bold", 36 * -1)
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.canvas.create_image(642.4243774414062, 456.0, image=self.image_image_5)

        self.figure = Figure(figsize=(5, 3), facecolor='white')
        self.ax = self.figure.add_subplot()
        self.canvas_graph = FigureCanvasTkAgg(self.figure, self)
        self.canvas_graph.get_tk_widget().place(x=361.42, y=318, width=553, height=260)

        self.auto_refresh_interval = 2000
        self.auto_refresh()

    def update_text(self):
        total_students = db_controller.get_total_amount_student()
        no_present = db_controller.get_total_amount_present()
        no_absent = db_controller.get_total_amount_absent()
        no_late = db_controller.get_total_amount_late()
        self.canvas.itemconfigure(self.total_student, text=total_students)
        self.canvas.itemconfigure(self.total_present, text=no_present)
        self.canvas.itemconfigure(self.total_absent, text=no_absent)
        self.canvas.itemconfigure(self.total_late, text=no_late)
        self.update_graph(no_present, no_absent, no_late)

    def update_graph(self, no_present, no_absent, no_late):
        self.ax.clear()
        accessories_data = {
            'category': ['Present', 'Absent', 'Late'],
            'amount': [no_present, no_absent, no_late]
        }
        colors = ['#FFA25F', '#FB3968', '#117EE4']
        self.ax.bar(accessories_data['category'], accessories_data['amount'], color=colors)
        self.ax.set_xlabel('Category')
        self.ax.set_ylabel('Amount')
        self.ax.set_title('Attendance Data')
        self.canvas_graph.draw()

    def auto_refresh(self):
        self.update_text()
        self.after(self.auto_refresh_interval, self.auto_refresh)



