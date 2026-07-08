from core.search.search_service import search_items
from core.database.initialize import initialize_database

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("RO Database Explorer - Public Edition")
        self.resize(1100, 700)

        root = QWidget()
        layout = QVBoxLayout(root)
        layout.setContentsMargins(24, 24, 24, 16)
        layout.setSpacing(16)

        title = QLabel("RO Database Explorer")
        title.setStyleSheet("font-size: 32px; font-weight: bold;")

        subtitle = QLabel("Public Edition v0.1.1 / RO情報ハブ")
        subtitle.setStyleSheet("font-size: 15px; color: #666;")

        search_row = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("アイテム名・モンスター名・カード名などを入力...")
        self.search_box.setMinimumHeight(42)

        search_button = QPushButton("検索")
        search_button.setMinimumHeight(42)
        search_button.clicked.connect(self.on_search)

        search_row.addWidget(self.search_box)
        search_row.addWidget(search_button)

        category_row = QHBoxLayout()
        categories = ["アイテム", "モンスター", "カード", "マップ", "NPC", "クエスト"]

        for name in categories:
            button = QPushButton(name)
            button.setMinimumHeight(40)
            category_row.addWidget(button)

        result_title = QLabel("検索結果")
        result_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.result_area = QLabel("まだデータはありません。\n次の段階でSQLiteと検索エンジンを接続します。")
        self.result_area.setAlignment(Qt.AlignCenter)
        self.result_area.setMinimumHeight(300)
        self.result_area.setStyleSheet(
            """
            QLabel {
                border: 1px solid #ccc;
                border-radius: 8px;
                background: #f7f7f7;
                color: #555;
                font-size: 16px;
            }
            """
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(search_row)
        layout.addLayout(category_row)
        layout.addWidget(result_title)
        layout.addWidget(self.result_area)

        self.setCentralWidget(root)

        status = QStatusBar()
        status.showMessage("Database: 未接続 / Version: 0.1.1 / Edition: Public")
        self.setStatusBar(status)


    def on_search(self):
        keyword = self.search_box.text().strip()

        if not keyword:
            self.result_area.setText("検索キーワードを入力してください。")
            return

        results = search_items(keyword)

        if not results:
            self.result_area.setText("検索結果はありません。")
            return

        lines = []
        for item_id, name in results:
            lines.append(f"{item_id}  {name}")

        self.result_area.setText("\n".join(lines))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    initialize_database()
    main()