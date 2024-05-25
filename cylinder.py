import tkinter as tk
from tkinter import filedialog, messagebox
import inventor
from inventor import *

class InputDialog(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Input Parameters for the Cylinder")
        self.geometry("400x300")

        self.label_radius = tk.Label(self, text="Enter the radius of the arc:")
        self.label_radius.pack(pady=5)
        self.entry_radius = tk.Entry(self)
        self.entry_radius.pack(pady=5)

        self.label_angle = tk.Label(self, text="Enter the angle of the arc (in degrees):")
        self.label_angle.pack(pady=5)
        self.entry_angle = tk.Entry(self)
        self.entry_angle.pack(pady=5)

        self.label_height = tk.Label(self, text="Enter the height of the cylinder:")
        self.label_height.pack(pady=5)
        self.entry_height = tk.Entry(self)
        self.entry_height.pack(pady=5)

        self.button_save_path = tk.Button(self, text="Select Save Directory", command=self.select_save_path)
        self.button_save_path.pack(pady=10)

        self.label_save_path = tk.Label(self, text="No directory selected")
        self.label_save_path.pack(pady=5)

        self.button_submit = tk.Button(self, text="Submit", command=self.submit)
        self.button_submit.pack(pady=10)

        self.save_path = None

    def select_save_path(self):
        self.save_path = filedialog.askdirectory(title="Select Save Directory")
        if self.save_path:
            self.label_save_path.config(text=self.save_path)
        else:
            self.label_save_path.config(text="No directory selected")

    def submit(self):
        try:
            self.radius = float(self.entry_radius.get())
            self.angle = float(self.entry_angle.get())
            self.height = float(self.entry_height.get())

            if not self.save_path:
                raise ValueError("Save path not selected")

            self.destroy()
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))

def get_user_input():
    dialog = InputDialog()
    dialog.mainloop()
    return dialog.radius, dialog.angle, dialog.height, dialog.save_path

def main():
    # this line closes all of the open parts
    com_obj().close_all_parts()

    # set document units
    units = 'imperial'

    # set it to overwrite file every time the part is instantiated (REMEMBER TO PUT SAVE AT THE BOTTOM!)
    overwrite = True

    # filename
    fname = 'cylinder.ipt'

    # get user input for radius, angle, height, and save path
    radius, angle, height, save_path = get_user_input()

    # setup part document 
    part = iPart(path=save_path, prefix=fname, units=units, overwrite=overwrite)

    # create workplane with zero offset on the xy plane
    wp = part.add_workplane(plane='xy')

    # attach a sketch to the above workplane
    sketch_1 = part.new_sketch(wp)

    # create a new structure, normally you would give it a start point, however here it is set to (0,0) by default
    s = structure(part, sketch_1)
    s.add_line_arc(start_angle=0, stop_angle=angle, radius=radius, flip_dir=True, rotation=0)

    # creates a closed path from the above structure
    test_path = s.draw_path(close_path=True)

    # extrude the part
    part.extrude(sketch_1, thickness=height, obj_collection=test_path, direction='positive', operation='join')

    # Fit the whole cavity in frame
    part.view.Fit()

    # save part
    part.save()

    # save stp part as copy of original
    part.save_copy_as(copy_as='stp')

if __name__ == "__main__":
    main()
