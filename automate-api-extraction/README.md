# Automate API Data Extraction

---

### Table of Contents

- [Objective](#objective)
- [Technologies](#technologies)
- [Project Files](#project-files)
- [Project Outcome](#project-outcome)
- [License](#license)
- [Author Info](#author-info)

---

## Objective

- Automate collection of cryptocurrency data from [Coin Market Cap API](https://coinmarketcap.com/api/).
- Write collected data into CSV file for further analysis.

[Back to the Top](#automate-api-data-extraction)

---

## Technologies

- Python

[Back to the Top](#automate-api-data-extraction)

---

## Project Files

The following are the files in this project.

- [Source Code](AutomateAPIExtraction.py)
- [Stored API Data File](api_data_collector.csv)

#### Key Tasks

- Connect to Coin Market API using the API Key.
- Create a new session and get the latest cryptocurrency listings.
- Design a dataframe with all the API data and the time the data was collected.
- Run the Collector Function a required number of times throughout the day to facilitate further analysis.
- Store this data in a CSV file every time the API data is collected.

**NOTE** - THE API KEY IS STORED IN A CONFIG FILE THAT HAS NOT BEEN ADDED TO THIS REPOSITORY. GET YOUR OWN API KEY FROM COINMARKET, ADD A CONFIG FILE AND STORE IT THERE

[Back to the Top](#automate-api-data-extraction)

---

## Project Outcome

- The resulting data was stored in a csv file [here](api_data_collector.csv)

[Back to the Top](#automate-api-data-extraction)

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

[Back to the Top](#automate-api-data-extraction)

---

## Author Info

- Github - [pras306](https://github.com/pras306)
- LinkedIn - [Prasanna Sriram](https://www.linkedin.com/in/prasanna-sriram/)

[Back to the Top](#automate-api-data-extraction)