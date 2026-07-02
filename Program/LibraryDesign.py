import customtkinter as ctk
import LibraryCode as lc
import MainMenuDesign as mmd

class ProgramDesign:
    def __init__(self, program):
        BtnMainMenu = ctk.CTkButton(program, text="create a presentation", command=lambda: self.LoadPage(self, program, mmd.ProgramDesign()))
        BtnMainMenu.pack()

    def LoadPage(self, program, PartDesign):
        for child in program.winfo_children():
            child.destroy()
        PartDesign()