from src import TrendsSeleniumUtils
from src.Utils import readCsv, getSeleniumInstanceFirefox, writeCsv
import logging
import time
import os
import argparse

INPUT_PATH = "input/"
OUTPUT_PATH = ""
DF_PROCESSED = "PROCESSED"
TRENDS_URL = "https://trends.google.com/trends"

def getSearchList(filename, keywordColumn):
    df = readCsv(filename , INPUT_PATH)
    if not DF_PROCESSED in df.columns:
        df[DF_PROCESSED] = "F"
    df = df[df[DF_PROCESSED] == "F"]
    return df, df[keywordColumn].values.tolist()

def fetchData(driver, keyword):
    driver.get(TRENDS_URL)
    time.sleep(2)

    TrendsSeleniumUtils.search(driver, keyword)
    TrendsSeleniumUtils.selectDate(driver)
    TrendsSeleniumUtils.downloadFile(driver)

def changeFileName(keyword, inputFilename, df):
    try:
        oldFileName = os.path.join(OUTPUT_PATH, "multiTimeLine.csv")
        if (os.path.exists(oldFileName)):
            newFileName = os.path.join(OUTPUT_PATH, "result_" + keyword + ".csv")
            os.rename(oldFileName, newFileName)
            writeCsv(df, INPUT_PATH, inputFilename)
    except:
        pass


def run(filename, keywordColumn):
    driver = getSeleniumInstanceFirefox(OUTPUT_PATH)
    df, searchList = getSearchList(filename, keywordColumn)
    totalKeywords = len(searchList)
    for index, keyword in enumerate(searchList):
        try:
            logging.info(f"{index}/{totalKeywords} Fetching data for {keyword}")
            df.loc[df[keywordColumn] == keyword, DF_PROCESSED] = 'T'
            fetchData(driver, keyword)
            changeFileName(keyword, filename, df)
        except Exception as e:
            logging.info(f"Error fetching data for {keyword}", e)
    driver.exit()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logging.info("Google Trends Scraper!\n")

    path = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_PATH = os.path.join(path, "output")

    parser = argparse.ArgumentParser(description='TrYp Scraper')
    parser.add_argument('--input_filename', required=True, help='input file containing keywords')
    parser.add_argument('--keyword_column', required=True, help='keywords column name')
    args = parser.parse_args()

    run(args.input_filename, args.keyword_column)
