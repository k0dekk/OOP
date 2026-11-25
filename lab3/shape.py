from abc import ABC, abstractmethod

BLACK = "black"
FILL_GRAY = "#c0c0c0"


class Shape(ABC):
    def __init__(self):
        self.xs1 = self.ys1 = self.xs2 = self.ys2 = 0

    def set(self, x1, y1, x2, y2):
        self.xs1, self.ys1, self.xs2, self.ys2 = x1, y1, x2, y2

    @abstractmethod
    def show(self, canvas):
        pass


class PointShape(Shape):
    def show(self, canvas):
        canvas.create_rectangle(self.xs1 - 1, self.ys1 - 1, self.xs1 + 1, self.ys1 + 1,
                                outline=BLACK, fill=BLACK, tags="shape")


class LineShape(Shape):
    def show(self, canvas):
        canvas.create_line(self.xs1, self.ys1, self.xs2, self.ys2,
                           fill=BLACK, tags="shape")


class RectShape(Shape):
    def show(self, canvas):
        canvas.create_rectangle(self.xs1, self.ys1, self.xs2, self.ys2,
                                outline=BLACK, fill="", tags="shape")


class EllipseShape(Shape):
    def show(self, canvas):
        canvas.create_oval(self.xs1, self.ys1, self.xs2, self.ys2,
                           outline=BLACK, fill=FILL_GRAY, tags="shape")
