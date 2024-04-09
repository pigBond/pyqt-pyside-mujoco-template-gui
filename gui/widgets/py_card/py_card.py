# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


from gui.uis.cards.ui_py_card import Ui_Card

class PyCard(QWidget):
    def __init__(self, parent=None):
        super(PyCard, self).__init__(parent)
        self.ui = Ui_Card()
        self.ui.setupUi(self)