import customtkinter as ctk
import preparing_presentation_code as ppc

class ProgramDesign:

    def __init__(self, program):
        start_presentation_btn = ctk.CTkButton(program,
                                               text="Start",
                                               )
        start_presentation_btn.pack()
        start_presentation_btn.configure(command=lambda : ProgramDesign.go_to_implementation_presentation(self, program))

    def go_to_implementation_presentation(self, program):
        for child in program.winfo_children():
            child.destroy()
        ppc.MainProgram(program=program)