import MainMenuDesign as md
import customtkinter as ctk

class App:
    def __init__(self):
        program = ctk.CTk()
        program.title("prelp")
        program.after(0, program.wm_state,'zoomed')
        md.ProgramDesign(program=program)
        program.mainloop()
App()