import pandas as pd
from utils.currency_dataframe import CurrencyDataframe
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"checking current work directory: {Path.cwd()}")

csvFile = r'.\data\global_inflation_data.csv'
currencyDf = CurrencyDataframe(csvFile).get_dataframe()

logging.info(f"Printing the first 5 rows of the dataframe")
print(currencyDf.head(5))