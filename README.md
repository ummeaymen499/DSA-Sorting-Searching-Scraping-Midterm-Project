DSA Pre-Midterm Project: Web Scraping, Sorting, and Searching Application
Project Overview
This project focuses on scraping a large dataset of entities (25,000+), with features for sorting, searching, and filtering. It includes a user interface (UI) that allows users to manage and visualize the data, leveraging algorithms studied in class as well as additional sorting and searching methods.

Table of Contents
Project Overview
Project Domain
Team Members
Features
Web Scraping
User Interface (UI)
Sorting
Searching
Multi-Level Sorting and Searching
Bonus Features
How to Run the Project
Dependencies
Project Structure
Contributing
Project Domain
For this project, we have chosen Mobiles as the target domain. The project involves scraping 25,000+ records of this entity, with multiple attributes, and providing interactive features to sort, search, and filter the data.

Team Members
This project is done in collaboration between the following group members:

Member 1: Umme Aymen (ummeaymen2005@gmail.com)
Member 2: Tayyabba Rajpoot 

Features
Web Scraping
Scraping 25,000+ Entities: The application scrapes at least 25,000 entities with 7 attributes for each entity.
Task Control: Users can start, stop, pause, and resume the scraping process. A progress bar visually shows the number of entities scraped.
Custom URL Input (Bonus): The UI allows users to input a URL for scraping data from different sources.
User Interface (UI)
Built with PyQT: The UI is designed using PyQT, offering a smooth and interactive experience.
Entity Display: The main page of the UI lists all the scraped entities in a tabular format, with the ability to sort and search through columns.
Sorting
Column Sorting: Each column in the table can be sorted. Users can select the sorting algorithm for each column, including both class-taught algorithms and additional algorithms.

Sorting Algorithms:

Taught Algorithms: Merge Sort, Quick Sort, Bubble Sort, etc.
Bonus Algorithms: Insertion Sort, Radix Sort, Tim Sort, etc.
Sorting Performance: After sorting, the application displays the sorting time in milliseconds, offering performance insights for each algorithm.

Searching
Column-Based Search: The UI allows searching based on individual columns. Users can choose from multiple search algorithms for each column.

Advanced String Search: Implement advanced filters for string columns such as:

Contains
Starts with
Ends with
Multi-Level Sorting and Searching
Multi-Column Sorting: Users can perform multi-level sorting across multiple columns, allowing for more complex ordering.

Composite Filters for Searching: Users can apply advanced search queries using logical operators such as AND, OR, and NOT across multiple columns.

Bonus Features
URL-Based Scraping: Users can provide a URL through the UI for custom scraping.
Progress Bar: A dynamic progress bar shows real-time progress of the scraping task.
How to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/ummeaymen499/DSA-Sorting-Searching-Scraping-Midterm-Project.git
cd DSA-PreMidProject
Install Dependencies: You can install the required Python libraries using pip:

bash
Copy code
pip install -r requirements.txt
Run the Application: To launch the UI and start the project:

bash
Copy code
python main.py
Usage:

Start Scraping: Click the "Start Scraping" button to begin scraping the entities.
Pause/Resume Scraping: Use the respective buttons to control the scraping process.
Sort Data: Click the column headers to sort the data and choose the sorting algorithm.
Search Data: Enter search criteria in the search box for each column and choose the search algorithm.
Dependencies
This project requires the following Python libraries:

PyQT5: For the user interface
BeautifulSoup4: For web scraping
Selenium: For dynamic web scraping
Pandas: For data handling and manipulation
Numpy: For algorithmic operations
You can install all dependencies using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Project Structure
bash
Copy code
DSA-PreMidProject/
│
├── src/                    # Source code
│   ├── scraping/            # Scraping logic
│   ├── sorting/             # Sorting algorithms
│   ├── searching/           # Searching algorithms
│   └── ui/                  # UI files
│
├── data/                    # Folder for storing scraped data
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── main.py                  # Main script to run the application
Contributing
We welcome contributions to enhance the project. To contribute:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-branch-name
Commit your changes: git commit -m 'Add new feature'
Push to the branch: git push origin feature-branch-name
Open a Pull Request.
