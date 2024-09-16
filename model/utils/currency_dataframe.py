import pandas as pd
from utils.currencies import currencies
import logging

class CurrencyDataframe:
    def __init__(self, file_path: str):
        self.file_path = file_path
        logging.info(f"Initialized CurrencyDataframe with file path: {self.file_path}")
    
    def _load_dataframe(self) -> pd.DataFrame:
        logging.info("Loading DataFrame from CSV file.")
        try:
            df = pd.read_csv(self.file_path)
            logging.info("DataFrame loaded successfully.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file.")
    
    def _transpose_dataframe(self) -> pd.DataFrame:
        logging.info("Transposing DataFrame.")
        df = self._load_dataframe()
        if 'indicator_name' not in df.columns or 'country_name' not in df.columns:
            raise ValueError("Required columns are missing in the DataFrame.")
        dfT = pd.melt(df.drop(columns=['indicator_name']), id_vars='country_name', var_name='Year', value_name='Inflation')
        logging.info("DataFrame transposed successfully.")
        return dfT 
        
    def _prepare_dataframe(self) -> pd.DataFrame:
        logging.info("Preparing DataFrame.")
        df = self._transpose_dataframe()
        currencyByCountry = {country: currency for currency, countries in currencies.items() for country in countries}
        df['Currency'] = df['country_name'].map(currencyByCountry)
        df['Year'] = df['Year'].astype(int)
        df = df[df['Year'] > 1995]
        df = df.dropna(subset=['Currency'])
        logging.info("DataFrame prepared successfully.")
        return df
    
    def _cumulative_sum(self) -> pd.DataFrame:
        logging.info("Calculating cumulative sum of inflation.")
        df = self._prepare_dataframe()
        df = df.sort_values(by=['country_name','Year'], ascending=[True, True])
        df['cumulative_inflation'] = df.groupby('country_name')['Inflation'].cumsum()
        logging.info("Cumulative sum calculated successfully.")
        return df
    
    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with cumulative inflation.")
        df = self._cumulative_sum()
        logging.info("Final DataFrame retrieved successfully.")
        return df