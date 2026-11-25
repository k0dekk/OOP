from editor import PointEditor, LineEditor, RectEditor, EllipseEditor

ZH = 18
MY_SHAPE_ARRAY_SIZE = ZH + 100


class ShapeObjectsEditor:
    def __init__(self):
        self.pcshape = []
        self.pse = None

    def _start(self, editor_class):
        self.pse = editor_class(self.pcshape, MY_SHAPE_ARRAY_SIZE)

    def start_point_editor(self):
        self._start(PointEditor)

    def start_line_editor(self):
        self._start(LineEditor)

    def start_rect_editor(self):
        self._start(RectEditor)

    def start_ellipse_editor(self):
        self._start(EllipseEditor)

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

    def on_init_menu_popup(self, checks):
        if self.pse:
            self.pse.on_init_menu_popup(checks)
        else:
            for var in checks:
                var.set(False)
