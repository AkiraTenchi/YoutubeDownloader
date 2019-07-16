#include "downloadwindow.h"
#include "ui_downloadwindow.h"

DownloadWindow::DownloadWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DownloadWindow)
{
    ui->setupUi(this);
}

DownloadWindow::~DownloadWindow()
{
    delete ui;
}
