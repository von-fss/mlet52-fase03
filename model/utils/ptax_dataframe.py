import pandas as pd
import logging


class PTaxlDataFrame:
    def __init__(self, file_path: str):
        self.file_path = file_path
        logging.info(f"Initialized AnpDataFrame with file path: {self.file_path}")

    def _load_dataframe(self) -> pd.DataFrame:
        logging.info("Loading DataFrame from CSV file.")
        try:
            df = pd.read_csv(self.file_path, sep=';', parse_dates=['data'])
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
        df['ano'] = df['data'].dt.year
        df['mes'] = df['data'].dt.month 
        df['dia'] = df['data'].dt.day 
        df.sort_values(by=['ano', 'mes', 'dia'], ascending=[True, True, True], inplace=True)
        df.drop(['cotacaoVenda', 'mes', 'dia'], axis=1, inplace=True)
        df = df.groupby(['ano']).last('cotacaoCompra').reset_index()
        df.rename(columns={'cotacaoCompra': 'ptax'}, inplace=True)
        logging.info("DataFrame prepared successfully.")
        return df        

    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with ptax by year.")
        df = self._prepare_dataframe()
        logging.info("Final DataFrame retrieved successfully.")
        return df                