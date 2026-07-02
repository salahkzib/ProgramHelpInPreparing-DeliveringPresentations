import cv2 as cv

class MainProgram:
    def __init__(self):
        self.start_presentation()

    def GetPixels(self):
        pass

    def basic_colors(self, image1, image2):
        pass

    def calcul_diff_pixels(self, image1, image2):
        pass

    def start_presentation(self):
        cap = cv.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('s'):
                break
        cap.release()
        cv.destroyAllWindows()

    def end_presentation(self):
        pass
