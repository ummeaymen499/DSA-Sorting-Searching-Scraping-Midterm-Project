from PyQt5.QtWidgets import QMessageBox

def start_scraping(scraping_thread, start_button, table_widget):
    if not scraping_thread.isRunning():
        start_button.setEnabled(False)
        table_widget.setRowCount(0)
        scraping_thread.start()
    else:
        QMessageBox.warning(None, "Warning", "Scraping is already in progress.")


def pause_scraping(scraping_thread, pause_button, start_button, load_data_func):
        if scraping_thread.isRunning():
            scraping_thread.pause()
            pause_button.setEnabled(False)
            start_button.setEnabled(True)
            load_data_func()
