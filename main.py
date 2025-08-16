from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_city.pressed.connect(self.but_add)

    def but_add(self):
        # Извлечение города с форматированием
        format_city = self.ui.user_city.text().strip().title()
        if self.ui.list_cities.count() != 0:
            if self.ui.curr_city.text()[-1].lower() != format_city[0].lower():
                QMessageBox.warning(
                    self,
                    "Предупреждение",
                    "Начальная буква введённого города не соотвутствует последней букве предыдущего города",
                )
                self.ui.user_city.clear()
                return 0
        # Добавляем город в список
        self.ui.list_cities.addItem(format_city)
        self.ui.curr_city.setText(format_city)
        self.ui.user_city.clear()
        self.ui.list_cities.sortItems()

    def keyPressEvent(self, e):
        # Если нажата кнопка "Enter" и строка непустая, добавляем город в список
        if e.key() in (Qt.Key_Return, Qt.Key_Enter) and self.ui.user_city.text().strip() != "":
            self.ui.add_city.click()


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    app.setWindowIcon(QIcon("icon.png"))
    win.show()
    app.exec()
