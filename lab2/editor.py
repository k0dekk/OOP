from abc import ABC, abstractmethod
from shape import PointShape, LineShape, RectShape, EllipseShape

RUBBER_COLOR = "red"


class Editor(ABC):
    @abstractmethod
    def on_lbdown(self, canvas, event): ...
    @abstractmethod
    def on_lbup(self, canvas, event): ...
    @abstractmethod
    def on_mouse_move(self, canvas, event): ...
    @abstractmethod
    def on_paint(self, canvas): ...


class ShapeEditor(Editor):
    shape_class = None

    def __init__(self, shapes):
        self.shapes = shapes
        self.drawing = False
        self.xstart = self.ystart = 0
        self.xend = self.yend = 0

    @abstractmethod
    def bounds(self):
        pass

    @abstractmethod
    def draw_trace(self, canvas, x1, y1, x2, y2):
        pass

    def on_lbdown(self, canvas, event):
        self.xstart = self.xend = event.x
        self.ystart = self.yend = event.y
        self.drawing = True

    def on_mouse_move(self, canvas, event):
        if not self.drawing:
            return
        canvas.delete("rubber")
        self.xend, self.yend = event.x, event.y
        self.draw_trace(canvas, *self.bounds())

    def on_lbup(self, canvas, event):
        if not self.drawing:
            return
        self.drawing = False
        canvas.delete("rubber")
        self.xend, self.yend = event.x, event.y
        if (self.xend, self.yend) != (self.xstart, self.ystart):
            self.add_shape(canvas, self.make_shape())
        self.on_paint(canvas)

    def on_paint(self, canvas):
        canvas.delete("shape")
        for shape in self.shapes:
            if shape:
                shape.show(canvas)

    def make_shape(self):
        shape = self.shape_class()
        shape.set(*self.bounds())
        return shape

    def add_shape(self, canvas, shape):
        if None in self.shapes:
            self.shapes[self.shapes.index(None)] = shape
        else:
            canvas.bell()


class PointEditor(ShapeEditor):
    shape_class = PointShape

    def on_lbdown(self, canvas, event):
        super().on_lbdown(canvas, event)
        self.drawing = False
        self.add_shape(canvas, self.make_shape())
        self.on_paint(canvas)

    def bounds(self):
        return self.xstart, self.ystart, self.xstart, self.ystart

    def draw_trace(self, canvas, x1, y1, x2, y2):
        pass


class LineEditor(ShapeEditor):
    shape_class = LineShape

    def bounds(self):
        return self.xstart, self.ystart, self.xend, self.yend

    def draw_trace(self, canvas, x1, y1, x2, y2):
        canvas.create_line(x1, y1, x2, y2, fill=RUBBER_COLOR, tags="rubber")


class RectEditor(ShapeEditor):
    shape_class = RectShape

    def bounds(self):
        return (2 * self.xstart - self.xend, 2 * self.ystart - self.yend,
                self.xend, self.yend)

    def draw_trace(self, canvas, x1, y1, x2, y2):
        canvas.create_rectangle(x1, y1, x2, y2, outline=RUBBER_COLOR, tags="rubber")


class EllipseEditor(ShapeEditor):
    shape_class = EllipseShape

    def bounds(self):
        return self.xstart, self.ystart, self.xend, self.yend

    def draw_trace(self, canvas, x1, y1, x2, y2):
        canvas.create_oval(x1, y1, x2, y2, outline=RUBBER_COLOR, tags="rubber")
