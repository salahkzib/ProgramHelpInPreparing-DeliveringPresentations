import preparing_presentation_design as ppd
import customtkinter as ctk
import mainmenu_code as mc

class ProgramDesign:
    def __init__(self, program):
        btn_create_presentation = ctk.CTkButton(program,
                                                text="create a presentation",
                                                command=lambda : ProgramDesign.go_to_making_presentation(self, program))
        btn_create_presentation.pack()

    def go_to_making_presentation(self, program):
        for child in program.winfo_children():
            child.destroy()
        ppd.ProgramDesign(program=program)
