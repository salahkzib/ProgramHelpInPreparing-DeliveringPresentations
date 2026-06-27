import customtkinter as ctk
import  delivering_presentation_design as dpd
from PIL import Image
import  numpy

class MainProgram:
    picture = None
    def __init__(self, program):
        pass
    def BasicColors(self, picture):
        def pp(x, y):
            z = (x, y)
            r = picture.getpixel(z)
            return r
        i = 0
        j = 0
        hp = picture.height
        wp = picture.width
        lst = list(pp(1, 1))
        arr_bc = [[lst, 1]]
        k = 0
        arr_pos_diff_pixs = ()
        while i < hp:
            while j < wp:
                l = 0
                while k < len(arr_bc):
                    com = arr_bc[k][0][0:3]
                    lst_new = list(pp(i, j))
                    if com == lst_new:
                        arr_bc[k][1] = arr_bc[k][1] + 1
                    else:
                        l += 1
                    k += 1
                if l == len(arr_bc):
                    lst_re = list(pp(i, j))
                    arr_bc.append([lst_re, 1])
                else:
                    pass
                k = 0
                j += 1
            j = 0
            i += 1
        print(len(arr_bc))
        print("f : ", arr_bc)
        return arr_bc
    def DifferentPixelsetector(self):
        pass
    def FramingDifference(self):
        pass
    def MesureDistances(self):
        pass
    def CheckClickWall(self):
        pass
