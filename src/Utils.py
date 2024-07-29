import os
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
from selenium import webdriver


def getSeleniumInstanceFirefox(downloadDir):
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = "/dev/null"
    ua = UserAgent()
    user_agent = ua.random
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.set_preference('browser.download.folderList', 2)  # custom location
    options.set_preference('browser.download.manager.showWhenStarting', False)
    options.set_preference('browser.download.dir', downloadDir)
    options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    firefoxService = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=firefoxService, options=options)
    return driver

def readCsv(fileName, inputDir):
    inputFilePath = os.path.join(inputDir, fileName)
    return pd.read_csv(inputFilePath)

def writeCsv(df, outputDir, outputFileName):
    outputFilePath = os.path.join(outputDir, outputFileName)
    df.to_csv(outputFilePath, sep=',', quotechar='"', encoding='utf-8', mode='w+', index=False)
