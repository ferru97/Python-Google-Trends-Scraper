import os
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
from selenium import webdriver


def getSeleniumInstanceFirefox(downloadDir, driver_path):
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = "/dev/null"
    ua = UserAgent()
    user_agent = ua.random
    options = Options()
    options.add_argument("user-agent="+user_agent)
    options.add_argument("user-agent="+user_agent)
    options.set_preference('browser.download.folderList', 2)  # custom location
    options.set_preference('browser.download.manager.showWhenStarting', False)
    options.set_preference('browser.download.dir', downloadDir)
    options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    if driver_path is None:
        driver_path = GeckoDriverManager().install()
    firefoxService = Service(driver_path)
    driver = webdriver.Firefox(service=firefoxService, options=options)
    return driver, driver_path

def readCsv(fileName, inputDir):
    inputFilePath = os.path.join(inputDir, fileName)
    return pd.read_csv(inputFilePath)

def writeCsv(df, outputDir, outputFileName):
    outputFilePath = os.path.join(outputDir, outputFileName)
    df.to_csv(outputFilePath, sep=',', quotechar='"', encoding='utf-8', mode='w+', index=False)
