import os
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog


class AskFileGraphical:
    def __init__(self, file_type: str, r_w: str) -> None:
        try:
            if r_w == "w":
                self.base_file = QFileDialog.getSaveFileName(filter=file_type)
            else:
                self.base_file = QFileDialog.getOpenFileName(filter=file_type)[0]
            self.file_name, self.file_extension = os.path.splitext(os.path.basename(self.base_file))
            self.file_dir = Path(self.base_file).resolve().parent
        except Exception as ex:
            self.base_file = ""
            self.file_name = ""
            self.file_dir = ""