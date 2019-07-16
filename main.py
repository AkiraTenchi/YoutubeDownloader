import sys
from qtpy import QtWidgets
import youtube_dl
import os
from YTDown.downloadwindow import Ui_DownloadWindow


app = QtWidgets.QApplication(sys.argv)


class DownloadWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DownloadWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("YouTube Downloader")

        self.ui.downloadBut.clicked.connect(self.download)

    def download(self):

        title = self.ui.titleLine.text()

        save_path = os.path.abspath(os.path.realpath("Songs") + f'/{title}.mp3')
        # save_path = save_path.replace(' ', '_')
        print(save_path)

        # download settings
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': save_path,
            'noplaylist': True,
            'nocheckcertificate': True,
            'proxy': "",
            'addmetadata': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        url = self.ui.urlLine.text()

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        self.ui.urlLine.setText('')
        self.ui.titleLine.setText('')


window = DownloadWindow()

window.show()

sys.exit(app.exec_())