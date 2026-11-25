from editor import PointEditor, LineEditor, RectEditor, EllipseEditor

ZH = 17
MY_SHAPE_ARRAY_SIZE = ZH + 100
TITLE = "Lab2"


class ShapeObjectsEditor:
    def __init__(self):
        self.pcshape = [None] * MY_SHAPE_ARRAY_SIZE
        self.pse = None

    def set_mode(self, window, editor, name):
        self.pse = editor
        window.title(f"{TITLE} - режим вводу: {name}")

    def start_point_editor(self, window):
        self.set_mode(window, PointEditor(self.pcshape), "крапки")

    def start_line_editor(self, window):
        self.set_mode(window, LineEditor(self.pcshape), "лінії")

    def start_rect_editor(self, window):
        self.set_mode(window, RectEditor(self.pcshape), "прямокутники")

    def start_ellipse_editor(self, window):
        self.set_mode(window, EllipseEditor(self.pcshape), "еліпси")

    def on_lbdown(self, canvas, event):
        if self.pse:
            self.pse.on_lbdown(canvas, event)

    def on_lbup(self, canvas, event):
        if self.pse:
            self.pse.on_lbup(canvas, event)

    def on_mouse_move(self, canvas, event):
        if self.pse:
            self.pse.on_mouse_move(canvas, event)

    def on_paint(self, canvas):
        if self.pse:
            self.pse.on_paint(canvas)
