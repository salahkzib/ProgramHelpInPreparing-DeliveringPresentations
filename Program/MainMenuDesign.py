import PreparingPresentationDesign as ppd
import LibraryDesign as ld
import CollaborationDesign as cd
import DeliveringPresentationDesign as dpd
import customtkinter as ctk
import MainMenuCode as mc

class ProgramDesign:
    def __init__(self, program):
        BtnCraeteNewPresentation = ctk.CTkButton(program,text="create a presentation", command=lambda : self.LoadPage(self, program, ppd.ProgramDesign()))
        BtnCraeteNewPresentation.pack()
        BtnStartPresentation = ctk.CTkButton(program,text = "start presentation", command=lambda :self.LoadPage(self, program, dpd.ProgramDesign()))
        BtnStartPresentation.pack()
        BtnMyLibrary = ctk.CTkButton(program,text = "my library", command=lambda :self.LoadPage(self, program, ld.ProgramDesign()))
        BtnMyLibrary.pack()
        BtnCollaboration = ctk.CTkButton(program,text = "collaboration", command=lambda :self.LoadPage(self, program, cd.ProgramDesign()))
        BtnCollaboration.pack()

    def LoadPage(self, program, PartDesign):
        for child in program.winfo_children():
            child.destroy()
        PartDesign()
