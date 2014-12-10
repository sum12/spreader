# to compile use pyinstaller
# bitness of the python interpreter
# determines the bitness of the software

from PyQt4 import QtCore, QtGui, QtNetwork, QtWebKit, Qt
import sip
import main_ui,pyperclip
import sys,os
import atexit
import ctypes

class UiBox(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowFlags(self.windowFlags() & 
                    (~QtCore.Qt.WindowContextHelpButtonHint))
        if sys.platform == 'win32':
            self.setWindowFlags(self.windowFlags() |
                        (QtCore.Qt.FramelessWindowHint))
        self.gui = main_ui.Ui_Dialog()
        self.gui.setupUi(self)
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.gui.dial_1,
                               QtCore.SIGNAL("valueChanged(int)"), self.dialChanged)
        QtCore.QObject.connect(self.gui.dial_2,
                               QtCore.SIGNAL("valueChanged(int)"), self.dialChanged)
        QtCore.QObject.connect(self.gui.dial_3,
                               QtCore.SIGNAL("valueChanged(int)"), self.dialChanged)
        QtCore.QObject.connect(self.gui.wordChunkSlider,
                               QtCore.SIGNAL("valueChanged(int)"), self.wordChunkSliderChanged)
        QtCore.QObject.connect(self.gui.newbtn,
                               QtCore.SIGNAL("clicked()"), self.newbtnClicked)

        QtCore.QObject.connect(self.gui.playPausebtn,
                               QtCore.SIGNAL("clicked()"), lambda : (self.timer.isActive() and (self.timer.stop() or self.gui.playPausebtn.setText('Play') or True) 
                                                                     or (self.timer.start() or self.gui.playPausebtn.setText('Pause'))))
        QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"),lambda:self.gui.label.setText(self.genr.next()))
        
        self.gui.playPausebtn.setEnabled(False)
        self.gui.dial_1.setValue(2)
        self.gui.dial_2.setValue(7)
        self.gui.dial_3.setValue(5)
        self.chunkSize = 1
        self.gui.wpmlabel.setText("WPM: %d"%self.wpm)
        self.timer.setInterval((60.0*1000)/self.wpm)
        self.gui.chunklabel.setText("Words Per Chunk: %d"%self.chunkSize)

    
    def dialChanged(self,int):
        self.wpm = self.gui.dial_1.value()*100+self.gui.dial_2.value()*10+self.gui.dial_3.value()
        self.timer.setInterval((60.0*1000)/self.wpm)
        self.gui.wpmlabel.setText("WPM: %d"%self.wpm)

    def wordChunkSliderChanged(self):
        self.chunkSize = self.gui.wordChunkSlider.value()
        self.gui.chunklabel.setText("Words Per Chunk: %d"%self.chunkSize)
        
    def newbtnClicked(self):
        text = pyperclip.winGetClipboard()
        self.gui.plainTextEdit.setPlainText( text or "No Text")
        self.genr = self.gengenr()
        self.gui.playPausebtn.setEnabled(True)

    def gengenr(self):
        word=''
        cnt=self.chunkSize-1
        self.gui.playPausebtn.setText('Pause')
        try:
            for i in self.gui.plainTextEdit_temp.toPlainText():
                if i not in ['\\','\n',' ']:
                    word+=i
                    continue
                elif cnt:
                    word+=i
                    cnt-=1
                    continue
                cnt=self.chunkSize-1
                yield word
                word=''
        finally:
            self.timer.stop()
            self.gui.playPausebtn.setText('Play')
            self.gui.playPausebtn.setChecked(False)
            self.genr = self.gengenr()
            yield word

class SApp(QtGui.QApplication):
    def __init__(self):
        QtGui.QApplication.__init__(self,[])
        #Set the style as windows else in ubuntu 13.04 it tries to load GTK which fails
        if sys.platform!='win32':
            self.setStyle("windows")






if __name__ == '__main__':
    app = SApp()
    ub = UiBox()
    ub.activateWindow()
    ub.show()
    os._exit(app.exec_())