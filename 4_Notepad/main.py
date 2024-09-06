import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Simple Notepad")

        # Set dark theme colors
        self.root.configure(bg="#2e2e2e")  # Dark background for the main window

        # Text widget with dark theme
        self.text_area: Text = Text(self.root, wrap="word", bg="#1e1e1e", fg="lightgreen", insertbackground="white", font=("Consolas", 12), padx=10, pady=10)
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Frame for buttons
        self.button_frame: Frame = Frame(self.root, bg="#2f2f2f")
        self.button_frame.pack(fill="x", padx=10, pady=5)

        # Save button
        self.save_button: Button = Button(self.button_frame, text="Save File", command=self.save_file, bg="#3e3e3e", fg="yellow", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Open button
        self.open_button: Button = Button(self.button_frame, text="Open File", command=self.open_file, bg="#3e3e3e", fg="yellow", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.open_button.pack(side=tk.RIGHT, padx=5)

        # Binding keyboard shortcuts
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-q>", lambda e: self.root.quit())
        self.root.bind("<Control-BackSpace>", lambda e: self.delete_current_word())

        # Initialize current file path
        self.current_file_path = None

    def save_file(self) -> None:
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f"File saved to {self.current_file_path}")
        else:
            self.save_file_as()

    def save_file_as(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.current_file_path = file_path
            self.save_file()

    def open_file(self) -> None:
        file_path: str = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.current_file_path = file_path
            print(f"File opened from {file_path}")

    def delete_current_word(self) -> None:
        cursor_index = self.text_area.index(tk.INSERT)
        line, column = map(int, cursor_index.split('.'))
        
        # Get the content of the current line
        line_content = self.text_area.get(f"{line}.0", f"{line}.end")
        
        # Find the start and end of the current word
        start = column
        while start > 0 and line_content[start - 1] not in (' ', '\t', '\n'):
            start -= 1
        
        end = column
        while end < len(line_content) and line_content[end] not in (' ', '\t', '\n'):
            end += 1
        
        # Delete the word
        self.text_area.delete(f"{line}.{start}", f"{line}.{end}")

    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root: Tk = Tk()
    app: SimpleNotepad = SimpleNotepad(root)
    app.run()

if __name__ == "__main__":
    main()