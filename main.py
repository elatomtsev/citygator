from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_city.pressed.connect(self.but_add)

    def but_add(self):
        # Извлечение города с форматированием
        self.format_city = self.ui.user_city.text().strip().title()
        # Добавляем город в список
        self.ui.list_cities.addItem(self.format_city)
        self.ui.curr_city.setText(self.format_city)
        self.ui.user_city.clear()
        self.ui.list_cities.sortItems()

    def keyPressEvent(self, e):
        # Если нажата кнопка "Enter" и строка непустая, добавляем город в список
        if e.key() in (Qt.Key_Return, Qt.Key_Enter) and self.ui.user_city.text().strip() != "":
            self.ui.add_city.click()

    # def upd_item(self):


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
