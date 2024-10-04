import pandas as pd
import logging


class BovespaDataFrame:

    #tamanho dos arquivos de leitura do arquivo da bovespa
    colspecs = [
        (2, 10),
        (10, 12),
        (12, 24),
        (27, 39),
        (56, 69),
        (69, 82),
        (82, 95),
        (108, 121),
        (152, 170),
        (170, 188)
    ]

    #nome dos campos
    namespecs = [
        'data_pregao',
        'codbdi',
        'sigla_acao',
        'nome_acao',
        'abertura',
        'maximo',
        'minimo',
        'fechamento',
        'qtd',
        'vol'
    ]

    def __init__(self, file_path: str):
        self.file_path = file_path
        logging.info(f"Initialized AnpDataFrame with file path: {self.file_path}")

    def _load_dataframe(self) -> pd.DataFrame:
        logging.info("Loading DataFrame from CSV file.")
        try:
            df = pd.read_fwf(self.file_path, colspecs=self.colspecs, names = self.namespecs, skiprows=1, encoding='latin1')
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
        df = df [df['codbdi'] == 2]        
        df.drop(['codbdi'], inplace=True, axis = 1)
        df['data_pregao'] = pd.to_datetime(df['data_pregao'], format = '%Y%m%d') #formatacao da data
        df['abertura'] = (df['abertura'] / 100).astype(float)
        df['maximo'] = (df['maximo'] / 100).astype(float)
        df['minimo'] = (df['minimo'] /100).astype(float)
        df['fechamento'] = (df['fechamento'] / 100).astype(float)
        #removi os outros preços para reduzir a memória
        df.drop(['abertura', 'maximo', 'minimo'], axis=1, inplace=True)
        logging.info("DataFrame prepared successfully.")
        return df        

    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with oil values by year.")
        df = self._prepare_dataframe()
        logging.info("Final DataFrame retrieved successfully.")
        return df                