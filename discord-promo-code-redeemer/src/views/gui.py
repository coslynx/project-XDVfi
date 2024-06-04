import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class PromoCodeRedeemerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Discord Promo Code Redeemer')
        self.setGeometry(100, 100, 400, 200)

        self.lbl_code = QLabel('Enter Promo Code:', self)
        self.lbl_code.move(50, 50)
        self.txt_code = QLineEdit(self)
        self.txt_code.move(150, 50)

        self.btn_redeem = QPushButton('Redeem Code', self)
        self.btn_redeem.move(150, 100)
        self.btn_redeem.clicked.connect(self.redeemCode)

        self.show()

    def redeemCode(self):
        promo_code = self.txt_code.text()
        # Add logic here to redeem the promo code on Discord server
        if promo_code:
            QMessageBox.information(self, 'Success', 'Promo code redeemed successfully!')
        else:
            QMessageBox.critical(self, 'Error', 'Invalid promo code. Please try again.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PromoCodeRedeemerGUI()
    sys.exit(app.exec_())