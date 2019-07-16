#ifndef DOWNLOADWINDOW_H
#define DOWNLOADWINDOW_H

#include <QMainWindow>

namespace Ui {
class DownloadWindow;
}

class DownloadWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit DownloadWindow(QWidget *parent = nullptr);
    ~DownloadWindow();

private:
    Ui::DownloadWindow *ui;
};

#endif // DOWNLOADWINDOW_H
