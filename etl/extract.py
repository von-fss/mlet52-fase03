from util.bovespa_dataframe import BovespaDataFrame
import pandas as pd 

df = BovespaDataFrame('2015').get_dataframe()
