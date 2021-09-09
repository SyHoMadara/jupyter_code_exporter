import os
from pathlib import Path
from tkinter import filedialog, Tk


class FileWithTkinter:
    def __init__(self, file_type: list) -> None:
        self.root = Tk()
        self.root.withdraw()
        self.base_file = filedialog.askopenfilename(filetypes=file_type)
        self.file_name, self.file_extension = os.path.splitext(os.path.basename(self.base_file))
        self.file_dir = Path(self.base_file).resolve().parent
