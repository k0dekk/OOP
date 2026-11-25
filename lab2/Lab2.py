import tkinter as tk
import tkinter.messagebox
from shape_editor import ShapeObjectsEditor, TITLE

soe = ShapeObjectsEditor()


def main():
    root = tk.Tk()
    root.title(TITLE)
    root.geometry("900x600")

    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=False)
    file_menu.add_command(label="Вихід", command=root.destroy)
    objects_menu = tk.Menu(menubar, tearoff=False)
    objects_menu.add_command(label="Крапка",       command=lambda: soe.start_point_editor(root))
    objects_menu.add_command(label="Лінія",        command=lambda: soe.start_line_editor(root))
    objects_menu.add_command(label="Прямокутник",  command=lambda: soe.start_rect_editor(root))
    objects_menu.add_command(label="Еліпс",        command=lambda: soe.start_ellipse_editor(root))
    menubar.add_cascade(label="Файл", menu=file_menu)
    menubar.add_cascade(label="Об'єкти", menu=objects_menu)
    root.config(menu=menubar)

    canvas.bind("<ButtonPress-1>",   lambda e: soe.on_lbdown(canvas, e))
    canvas.bind("<ButtonRelease-1>", lambda e: soe.on_lbup(canvas, e))
    canvas.bind("<Motion>",          lambda e: soe.on_mouse_move(canvas, e))
    canvas.bind("<Configure>",       lambda e: soe.on_paint(canvas))

    root.mainloop()


if __name__ == "__main__":
    main()
