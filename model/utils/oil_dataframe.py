import pandas as pd
import logging


class OilDataFrame:
    def __init__(self, file_path: str):
        self.file_path = file_path
        logging.info(f"Initialized AnpDataFrame with file path: {self.file_path}")

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
        

    def _prepare_dataframe(self) -> pd.DataFrame:
        df = self._load_dataframe()
        df.rename(columns={'Oil price - Crude prices since 1861 (current US$)': 'oil', 'Year': 'ano'}, inplace=True)        
        df.drop(['Code', 'Entity'], axis=1, inplace=True)
        #df = df.pivot(index=['ano'], columns='tipo', values='valor').reset_index()
        logging.info("DataFrame prepared successfully.")
        return df        

    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with oil values by year.")
        df = self._prepare_dataframe()
        logging.info("Final DataFrame retrieved successfully.")
        return df                