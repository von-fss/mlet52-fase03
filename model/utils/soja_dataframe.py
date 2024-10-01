import pandas as pd
import logging


class SojaDataFrame:
    def __init__(self, file_path: str):
        self.file_path = file_path
        logging.info(f"Initialized AnpDataFrame with file path: {self.file_path}")

    def _load_dataframe(self) -> pd.DataFrame:
        logging.info("Loading DataFrame from CSV file.")
        try:
            df = pd.read_excel(self.file_path, skiprows=3)
            logging.info("DataFrame loaded successfully.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file.")
        

    def _prepare_dataframe(self) -> pd.DataFrame:
        df = self._load_dataframe()
        df.drop(['À vista US$'], axis=1, inplace=True)
        df.rename(columns={'Data': 'ano', 'À vista R$': 'valor'}, inplace=True)
        logging.info("DataFrame prepared successfully.")
        return df        

    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with soja values by year.")
        df = self._prepare_dataframe()
        logging.info("Final DataFrame retrieved successfully.")
        return df                