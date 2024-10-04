import pandas as pd
import logging
import requests

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
        logging.info(f"Initialized B3DataFrame with file path: {self.file_path}")

    def _load_dataframe(self) -> pd.DataFrame:
        self._download_file()
        logging.info("Loading DataFrame from CSV file.")
        file_source = r'source\\' + self.file_path + '.zip'
        
        try:
            df = pd.read_fwf(file_source, compression='zip', colspecs=self.colspecs, names = self.namespecs, skiprows=1, encoding='latin1')        
            logging.info("DataFrame loaded successfully.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file.")
        
    def _download_file(self):
        logging.info('Download file from Bovespa')
        url = r'https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A' + self.file_path + '.ZIP'
        target = r'source\\' + self.file_path + '.zip'
        r = requests.get(url, verify=False)
        with open(target, 'wb') as f:
            f.write(r.content)
        logging.info('File saved successfully')

    def _save_data_lake(self, df):
        logging.info('Start to save pos processed file')
        df.to_parquet(r'data\\' + self.file_path)
        logging.info('File saved')


    def _prepare_dataframe(self) -> pd.DataFrame:
        df = self._load_dataframe()
        df = df [df['codbdi'] == 2]        
        df.drop(['codbdi'], inplace=True, axis = 1)
        df['data_pregao'] = pd.to_datetime(df['data_pregao'], format = '%Y%m%d') #formatacao da data
        df['abertura'] = (df['abertura'] / 100).astype(float)
        df['maximo'] = (df['maximo'] / 100).astype(float)
        df['minimo'] = (df['minimo'] /100).astype(float)
        df['fechamento'] = (df['fechamento'] / 100).astype(float)
        #filtro de apenas petrobras
        df[ df['sigla_acao'] == 'PETR4']        
        #removi os outros preços para reduzir a memória
        df.drop(['abertura', 'maximo', 'minimo', 'sigla_acao', 'nome_acao', 'qtd', 'vol'], axis=1, inplace=True)

        logging.info("DataFrame prepared successfully.")
        return df        

    def get_dataframe(self) -> pd.DataFrame:
        logging.info("Getting final DataFrame with B3 data by year.")
        df = self._prepare_dataframe()
        self._save_data_lake(df)
        logging.info("Final DataFrame retrieved successfully.")        
        return df                