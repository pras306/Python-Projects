# Projects in Python

---

### Table of Contents

- [Projects](#projects)
- [License](#license)
- [Author Info](#author-info)

---

## Projects

This repository contains my data analysis projects which I have worked using Python.

### [Automate API Data Extraction](automate-api-extraction/AutomateAPIExtraction.py)

#### Objective

- Automate collection of cryptocurrency data from [Coin Market Cap API](https://coinmarketcap.com/api/).
- Write collected data into CSV file for further analysis.

#### Key Tasks

- Connect to Coin Market API using the API Key.
- Create a new session and get the latest cryptocurrency listings.
- Design a dataframe with all the API data and the time the data was collected.
- Run the Collector Function a required number of times throughout the day to facilitate further analysis.
- Store this data in a CSV file every time the API data is collected.

#### Outcome

- The resulting data was stored in a csv file [here](automate-api-extraction/api_data_collector.csv)


### [Automate File Sorter](automate-file-sorter/AutomaticFileSorter.py)

#### Objective

- Automate sorting of different types of files based on the file types
- Create Folders for each type and store the files in appropriate folders.

#### Key Tasks

- Create a list of all the different files in the destination folder.
- For each file,
    - Check if there is a folder for the current file type.
    - If there is a folder, move the file into the folder
    - If there is not, create a new folder and move the file into the new folder.
- Repeat the above process for all the files.

#### Outcome

- The files were stored in appropriate folders. Check the folder [here](automate-file-sorter/Files)


### [Web Scrapper](web-scrapper/AmazonWebScrapper.py)

#### Objective

- Create a web scrapper that gathers data about books from Amazon.
- Create a web scrapper that collects data about top companies in the US from Wikipedia.

#### Key Tasks

- Connect to the repective websites using a web scrapper like Beautiful Soup.
- Perform exploratory data analysis to see which data is required to be gathered.
- Store the necessary data in tables.
- Check to see if the data needs to be transformed for better analysis.
- Store this data in a CSV file.

#### Outcome

- The resulting data from Amazon Books was stored in a csv file [here](web-scrapper/Amazon_Books.csv) and data about the top companies in the US was stored [here](web-scrapper/Companies.csv)


### [Data Cleaning](data-cleaning/PandasDataCleaning.py)

#### Objective

- Objective of this project is to clean the [Customer Call data](data-cleaning/CustomerCallList.xlsx) provided to us.
- Perform data cleaning and transformation and prepare data for futher analysis.

#### Key Tasks

- Perform a check for removing duplicates, unwanted columns and unwanted data.
- Standardize the format in the phone number column.
- Split the address column to normalize it.
- Standardize the Paying customer and Do not contact columns.
- Remove the null values and customers who have requested not to be contacted.
- Write final data into a CSV file for further analysis.

#### Outcome

- The cleaned and transformed data was stored [here](data-cleaning/FinalList.csv)

[Back to the Top](#projects-in-python)

---

## License

MIT License

Copyright (c) [2024] [Prasanna Sriram]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back to the Top](#projects-in-python)

---

## Author Info

- Github - [pras306](https://github.com/pras306)
- LinkedIn - [Prasanna Sriram](https://www.linkedin.com/in/prasanna-sriram/)

[Back to the Top](#projects-in-python)