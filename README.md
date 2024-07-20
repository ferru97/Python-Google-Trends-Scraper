# Google Trends Scraper
Python Google Trands Scraper using Selenium 
### Usage
Install dependencies:
```sh
pip install -r requirements.txt
```
Place the input csv file containing the keywords in the *input* directory and run
```sh
py main.py --input_filename input_file_name.csv --keyword_column column_containing_keywords
```
The scripts adds a new column on the input csv file named *PROCESSED* and has value *T* if the keyword has been processed of *F* otherwise. 
If a record has *PROCESSED = F*, it gets skipped

The script creates an output file for each keyword in the *output* folder
