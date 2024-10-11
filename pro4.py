import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, pyqtSignal, QObject, QThread, QMutex, QWaitCondition
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from my_form import Ui_Dialog
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pro1 import ScraperThread 

from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from Sorting.ScrappingFunctions import pause_scraping, start_scraping
from Sorting.DataSorter import shell_sort,bubble_sort,insertion_sort,selection_sort,merge_sort,quick_sort,heap_sort,counting_sort,radix_sort,bucket_sort,cocktail_shaker_sort
from Sorting.MultiDataSorter import multiheap_sort,multi_bubble_sort,multi_bucket_sort,multi_cocktail_shaker_sort,multi_counting_sort,multi_insertion_sort,multi_merge_sort,multi_quick_sort,multi_radix_sort,multi_selection_sort,multi_shell_sort


sys.setrecursionlimit(15000)

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.table_widget = self.ui.QTableWidget
        
        # Connect buttons
        self.ui.pushButton_2.clicked.connect(self.sort_column)
        self.ui.pushButton_3.clicked.connect(self.search_column)
        self.ui.pushButton_6.clicked.connect(self.multi_sort)
        self.ui.pushButton_5.clicked.connect(self.multi_search)
        self.ui.pushButton_4.clicked.connect(self.handle_pause_scraping)
        self.ui.pushButton_7.clicked.connect(self.handle_start_scraping)
        
        self.scraping_thread = ScraperThread()  # Initialize the scraper thread
        self.scraping_thread.data_scraped.connect(self.handle_scraped_data)  # Connect the signal to the handler

        # Connect header click signal to handle_column_click
        self.table_widget.horizontalHeader().sectionClicked.connect(self.handle_column_click)

        self.load_data()
        self.selected_column_index = -1

    def load_data(self):
        # Load data from CSV file
        try:
            self.data = pd.read_csv('E:/DSA/combined_ebay_mobile_data.csv')
            self.table_widget.setRowCount(self.data.shape[0])
            self.table_widget.setColumnCount(self.data.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.data.columns.tolist())
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "File not found. Please check the file path.")

    def handle_start_scraping(self):
        start_scraping(self.scraping_thread, self.ui.pushButton_7, self.table_widget)

    def handle_pause_scraping(self):
        pause_scraping(self.scraping_thread, self.ui.pushButton_4, self.ui.pushButton_7, self.load_data_from_csv)

    def load_data_from_csv(self):
        # Load the data from the CSV file into the table
        try:
            df = pd.read_csv('scrapedurl.csv')  # Adjust the file path if needed
            self.table_widget.setRowCount(df.shape[0])  # Clear existing rows
            self.table_widget.setColumnCount(df.shape[1])
            self.table_widget.setHorizontalHeaderLabels(df.columns.tolist())
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "CSV file not found. Please run the scraper first.")

    def handle_scraped_data(self, df):
        # Update the table with scraped data
        df.to_csv('scraped_data.csv', index=False)  # Save the scraped data to CSV
        self.table_widget.setRowCount(df.shape[0])
        self.table_widget.setColumnCount(df.shape[1])
        self.table_widget.setHorizontalHeaderLabels(df.columns.tolist())
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))


    def handle_column_click(self, column_index):
        # Handles the column click and stores the selected column index.
        print(f"Column {column_index} clicked")
        self.selected_column_index = column_index  # Save the clicked column index
        column_name = self.data.columns[column_index]  # Get the column name
        print(f"Selected column: {column_name}")
    def clean_value(value):
        if pd.isna(value) or "not found" in value.lower() or "not specified" in value.lower() or "free" in value.lower():
            return None
        match = re.search(r'\$([\d,]+(?:\.\d{2})?)', value)
        return float(match.group(1).replace(',', '')) if match else None
    def update_table(self, data):
        # Update the QTableWidget with scraped data
        if isinstance(data, list) and len(data) > 0:
            # Clear previous data
            self.table_widget.setRowCount(0)
            self.data = pd.DataFrame(data)
            self.table_widget.setRowCount(self.data.shape[0])
            self.table_widget.setColumnCount(self.data.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.data.columns.tolist())
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))
        else:
            QMessageBox.warning(self, "Warning", "No data scraped.")

    def multi_sort(self):
        col_1 = self.ui.comboBox_5.currentText()
        col_2 = self.ui.comboBox_6.currentText()

        algo_1 = self.ui.comboBox_4.currentText()  # Get selected algorithm

        print(algo_1)

        # Define numeric columns for specific sorting algorithms
        numeric_columns = ['Price', 'Seller Info', 'Shipping Cost', 'Quantity Sold']

        start_time = QTime.currentTime()  # Start time for performance measurement

        # Check if selected algorithms require numeric columns
        if algo_1 in ["Counting Sort", "Radix Sort", "Bucket Sort"]:
            if col_1 not in numeric_columns or col_2 not in numeric_columns:
                self.show_error_message("Error: Counting Sort, Radix Sort, and Bucket Sort require both columns to be numeric (Price, Seller Info, Shipping Cost, Quantity Sold).")
                return

        # Proceed with sorting based on the selected algorithm
        if algo_1 == "Heapify Sort":
            multiheap_sort(self.data, col_1, col_2)
            self.update_table()  

        elif algo_1 == "Insertion Sort":
            multi_insertion_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Bubble Sort":
            multi_bubble_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Selection Sort":
            multi_selection_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Merge Sort":
            multi_merge_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Quick Sort":
            multi_quick_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Counting Sort":
            multi_counting_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Radix Sort":
            multi_radix_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Bucket Sort":
            multi_bucket_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Shell Sort":
            multi_shell_sort(self.data,col_1, col_2)
            self.update_table()  

        elif algo_1 == "Cocktail Shaker Sort":
            multi_cocktail_shaker_sort(self.data,col_1, col_2)
            self.update_table()  

        else:
            self.show_error_message("Unknown sorting algorithm selected.")

        elapsed_time = start_time.msecsTo(QTime.currentTime())
        print(f"Sorting completed in {elapsed_time} ms")
        self.update_time_display1(elapsed_time)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # Show the message box
    def sort_column(self):
        # Sort the column selected by clicking the header.
        if self.selected_column_index == -1:
            print("No column selected. Please click on a column header to select.")
            return

        selected_column = self.data.columns[self.selected_column_index]  # Use the clicked column
        selected_algorithm = self.ui.comboBox.currentText()  # Get selected algorithm
        print(f"Selected Algorithm: {selected_algorithm} for column: {selected_column}")

        # Define numeric columns for specific sorting algorithms
        numeric_columns = ['Price', 'Seller Info', 'Shipping Cost', 'Quantity Sold']
        if selected_algorithm in ["Counting Sort", "Radix Sort", "Bucket Sort"]:
            if selected_column not in numeric_columns:
                self.show_error_message(
                    "Error: Counting Sort, Radix Sort, and Bucket Sort can only be applied to the following numeric columns: "
                    f"{', '.join(numeric_columns)}."
                )
                return

        start_time = QTime.currentTime() 
        if selected_algorithm == "Bubble Sort":
            val1, val2 = bubble_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table()           
        elif selected_algorithm == "Insertion Sort ":
            val1, val2 = insertion_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Selection Sort":
            val1, val2 = selection_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Merge Sort ":
            val1, val2 = merge_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Quick Sort":
            val1, val2 = quick_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Counting Sort":
            val1, val2 = counting_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Radix Sort":
            val1, val2 = radix_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Bucket Sort":
            val1, val2 = bucket_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table()     
        elif selected_algorithm == "Heapify Sort":
            val1, val2 = heap_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Cocktail Shaker Sort":
            val1, val2 = cocktail_shaker_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table() 
        elif selected_algorithm == "Shell Sort":
            val1, val2 = shell_sort(self.data, selected_column)  
            self.data[val1] = val2  
            self.update_table()  
        else:
            print("Unknown sorting algorithm selected.")

        elapsed_time = start_time.msecsTo(QTime.currentTime())
        print(f"Sorting completed in {elapsed_time} ms")
        self.update_time_display(elapsed_time)
    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # Show the message box

    def search_column(self):
        if self.selected_column_index == -1:
            QMessageBox.warning(self, "Warning", "Please select a column to search.")
            return

        column_name = self.data.columns[self.selected_column_index]
        filter_text = self.ui.lineEdit.text()  # Assuming you have a QLineEdit for input
        filter_type = self.ui.comboBox_filter.currentText()  
        if not filter_text.strip():  # Using strip() to ignore whitespace
            QMessageBox.warning(self, "Warning", "Please enter a search term.")
            return
        if filter_type == "Contains":
            filtered_data = self.data[self.data[column_name].str.contains(filter_text, na=False)]
        elif filter_type == "Starts With":
            filtered_data = self.data[self.data[column_name].str.startswith(filter_text, na=False)]
        elif filter_type == "Ends With":
            filtered_data = self.data[self.data[column_name].str.endswith(filter_text, na=False)]
        else:
            QMessageBox.warning(self, "Warning", "Unknown filter type selected.")
            return
        if filtered_data.empty:
            QMessageBox.warning(self, "Warning", "No results found for the given search term.")
            return

        self.table_widget.setRowCount(filtered_data.shape[0])
        self.table_widget.setColumnCount(filtered_data.shape[1])
        self.table_widget.setHorizontalHeaderLabels(filtered_data.columns.tolist())
        for i in range(filtered_data.shape[0]):
            for j in range(filtered_data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(filtered_data.iat[i, j])))

    def search_column(self):
        try:
            # Check if a column is selected
            if self.selected_column_index == -1:
                print("No column selected. Please click on a column header to select.")
                return
            search_text = self.ui.lineEdit_2.text().strip().lower()  # Get the search text from the input field
            selected_column = self.data.columns[self.selected_column_index]  # Get the selected column based on user click
            print(f"Searching for '{search_text}' in column: {selected_column}")
            search_type = self.ui.comboBox_2.currentText()
            if search_type == "Contains":
                filtered_data = self.data[self.data[selected_column].astype(str).str.lower().str.contains(search_text, na=False)]
            elif search_type == "Starts withs":
                filtered_data = self.data[self.data[selected_column].astype(str).str.lower().str.startswith(search_text)]
            elif search_type == "Ends withs":
                filtered_data = self.data[self.data[selected_column].astype(str).str.lower().str.endswith(search_text)]
            else:
                print("Invalid search type selected.")
                return
            if filtered_data.empty:
                print("No matches found.")
                self.table_widget.setRowCount(0)  
                self.load_original_data()  # Call a function to reload original data in the grid
                return
            self.table_widget.setRowCount(filtered_data.shape[0])  # Set the row count of the table
            for i in range(filtered_data.shape[0]):
                for j in range(filtered_data.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(filtered_data.iat[i, j])))
        except Exception as e:
            print(f"An error occurred: {e}")
    def load_original_data(self):
        self.table_widget.setRowCount(self.data.shape[0])  # Set the row count based on the original data
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))
    def update_table(self):
        # Update the table widget with sorted data
        self.table_widget.setRowCount(self.data.shape[0])
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))
        
     
    def update_time_display(self, elapsed_time):
        self.ui.timeLabel.setText(f"{elapsed_time:.6f} ms")
    def update_time_display1(self, elapsed_time):
        self.ui.timeLabel_2.setText(f"{elapsed_time:.6f} ms")

    def multi_search(self):
        # Get the filter inputs from the UI
        filter_1 = self.ui.lineEdit_3.text().lower().strip()  # Brand filter input
        filter_2 = self.ui.lineEdit_4.text().lower().strip()  # Location "not found" filter input
        operator = self.ui.comboBox_3.currentText().strip()  
        columns_to_filter = list(range(7))  
        for row in range(self.table_widget.rowCount()):
            self.table_widget.hideRow(row)  
        any_row_shown = False
        for row in range(self.table_widget.rowCount()):
            # Get the text from the specified columns
            column_texts = []
            for col in columns_to_filter:
                item = self.table_widget.item(row, col)
                text = item.text().lower().strip() if item else ''
                column_texts.append(text)
            show_row = False
            if operator == 'AND':
                # Show row if it contains the brand and does not contain the location filter
                show_row = (any(filter_1 in text for text in column_texts) and 
                            any(filter_2  in text for text in column_texts))
            elif operator == 'OR':
                # Show row if it contains the brand or does not contain the location filter
                show_row = (any(filter_1 in text for text in column_texts) or 
                            any(filter_2  in text for text in column_texts))
            elif operator == 'NOT':
                show_row = (all(filter_1 not in text for text in column_texts) and 
                            all(filter_2 not in text for text in column_texts))
            if show_row:
                self.table_widget.showRow(row)
                any_row_shown = True 
        if not any_row_shown:
            print("No rows match the filtering criteria.")  # Debugging
        else:
            print("Filtering complete.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.show()
    sys.exit(app.exec_())