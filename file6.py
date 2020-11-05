from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QWidget()
lb1 = QLineEdit(win)
ln1 = QLineEdit()
ln2 = QLineEdit()

def window():
    form = QFormLayout(win)
    nm = QLabel()
    nm.setText("Panjang")
    form.addRow(nm, ln1)

    nm = QLabel()
    nm.setText("Lebar")
    form.addRow(nm, ln2)
    
    btn1 = QPushButton()
    btn1.setText("Keliling Persegi Panjang")
    btn1.clicked.connect(hitung)
    form.addRow(btn1)

    form.addRow(lb1)

    win.setGeometry(100, 100, 500, 300)
    win.setWindowTitle("PyQt signal")
    win.show()
    sys.exit(app.exec_())

def hitung():
    try:
        bil1 = int(ln1.text())
    except ValueError:
        lb1.setText("Panjang yang anda masukkan bukan angka")
    else :
        try :
            bil2 = int(ln2.text())
        except ValueError:
            lb1.setText("Lebar yang anda masukkan bukan angka")
        else :
            hasil = 2*(bil1+bil2)
            lb1.setText("Hasil: " + str(hasil))

if __name__ == "__main__":
    window()

