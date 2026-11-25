import tkinter as tk
import tkinter.messagebox
from shape_editor import ShapeObjectsEditor
from toolbar import ToolBar

TITLE = "Lab3"

OBJECTS = [("point", "point", "Крапка"),
           ("line", "line", "Лінія"),
           ("rect", "rect", "Прямокутник"),
           ("ellipse", "ellipse", "Еліпс")]


class MainWindow:
    def __init__(self):
        self.soe = ShapeObjectsEditor()
        self.root = tk.Tk()
        self.root.title(TITLE)
        self.root.geometry("900x600")
        self.on_create()

    def on_create(self):
        self.create_menu()
        self.toolbar = ToolBar(self.root, [(name, kind, text, lambda i=i: self.choose_mode(i))
                                           for i, (name, kind, text) in enumerate(OBJECTS)])
        self.toolbar.pack(side="top", fill="x")
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        c = self.canvas
        c.bind("<ButtonPress-1>",   lambda e: self.soe.on_lbdown(c, e))
        c.bind("<ButtonRelease-1>", lambda e: self.soe.on_lbup(c, e))
        c.bind("<Motion>",          lambda e: self.soe.on_mouse_move(c, e))
        c.bind("<Configure>",       lambda e: self.soe.on_paint(c))

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Вихід", command=self.root.destroy)
        self.checks = [tk.BooleanVar(value=False) for _ in OBJECTS]
        self.objects_menu = tk.Menu(menubar, tearoff=False, postcommand=self.on_init_menu_popup)
        for i, (name, kind, text) in enumerate(OBJECTS):
            self.objects_menu.add_checkbutton(label=text, variable=self.checks[i],
                                              command=lambda i=i: self.choose_mode(i))
        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="Про програму", command=self.on_about)
        menubar.add_cascade(label="Файл", menu=file_menu)
        menubar.add_cascade(label="Об'єкти", menu=self.objects_menu)
        menubar.add_cascade(label="Довідка", menu=help_menu)
        self.root.config(menu=menubar)

    def choose_mode(self, index):
        (self.soe.start_point_editor, self.soe.start_line_editor,
         self.soe.start_rect_editor, self.soe.start_ellipse_editor)[index]()
        self.toolbar.press_button(index)

    def on_init_menu_popup(self):
        self.soe.on_init_menu_popup(self.checks)

    def on_about(self):
        tk.messagebox.showinfo("Про програму", "Lab3: графічний редактор з панеллю інструментів\nВаріант Ж = 18")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    MainWindow().run()
