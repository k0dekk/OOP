import tkinter as tk

ICON_SIZE = 24
BLACK = "#000000"
GRAY = "#c0c0c0"


def make_icon(kind):
    img = tk.PhotoImage(width=ICON_SIZE, height=ICON_SIZE)
    c = ICON_SIZE // 2

    def dot(x, y, color=BLACK):
        img.put(color, (x, y))

    if kind == "point":
        for y in range(ICON_SIZE):
            for x in range(ICON_SIZE):
                if (x - c) ** 2 + (y - c) ** 2 <= 9:
                    dot(x, y)
    elif kind == "line":
        for i in range(4, 21):
            dot(i, 24 - i)
            dot(i, 23 - i)
    elif kind == "rect":
        for x in range(3, 21):
            for y in (5, 6, 17, 18):
                dot(x, y)
        for y in range(5, 19):
            for x in (3, 4, 19, 20):
                dot(x, y)
    elif kind == "ellipse":
        a, b = 10, 7
        for y in range(ICON_SIZE):
            for x in range(ICON_SIZE):
                r = ((x - c) / a) ** 2 + ((y - c) / b) ** 2
                if r <= 0.62:
                    dot(x, y, GRAY)
                elif r <= 1.0:
                    dot(x, y)
    return img


class ToolTip:
    def __init__(self, widget, get_text, delay=450):
        self.widget, self.get_text, self.delay = widget, get_text, delay
        self.tip = None
        self.job = None
        widget.bind("<Enter>", self.on_enter, add="+")
        widget.bind("<Leave>", self.on_leave, add="+")
        widget.bind("<ButtonPress>", self.on_leave, add="+")

    def on_enter(self, event):
        self.job = self.widget.after(self.delay, self.show)

    def on_leave(self, event=None):
        if self.job:
            self.widget.after_cancel(self.job)
            self.job = None
        if self.tip:
            self.tip.destroy()
            self.tip = None

    def show(self):
        x = self.widget.winfo_rootx() + 4
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 4
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry(f"+{x}+{y}")
        tk.Label(self.tip, text=self.get_text(), background="#ffffe1",
                 relief="solid", borderwidth=1, padx=4, pady=1).pack()


class ToolBar(tk.Frame):
    def __init__(self, parent, buttons):
        super().__init__(parent, relief="raised", borderwidth=1)
        self.tips = {}
        self.buttons = []
        self.icons = []
        for i, (bid, kind, text, command) in enumerate(buttons):
            icon = make_icon(kind)
            self.icons.append(icon)
            b = tk.Button(self, image=icon, command=command, relief="raised", borderwidth=2)
            b.pack(side="left", padx=1, pady=1)
            self.buttons.append(b)
            self.tips[bid] = text
            ToolTip(b, lambda bid=bid: self.need_text(bid))

    def need_text(self, button_id):
        return self.tips.get(button_id, "Щось невідоме")

    def press_button(self, index):
        for i, b in enumerate(self.buttons):
            b.config(relief="sunken" if i == index else "raised")
