from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.teste import Teste

class dbSqlServer(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(dbSqlServer, cls).__new__(cls)

        mssql_engine = create_engine( "mssql+pyodbc://megauser:megamente123!@fiapdb.database.windows.net:1433/fiapdb?driver=ODBC+Driver+17+for+SQL+Server",
                                     # disable default reset-on-return scheme
                                     pool_reset_on_return=None)
        # session = Session(mssql_engine)
        # stmt = select(Teste)        
        # for item in session.scalars(stmt):
        #     print(item)

        return cls.instance

dbSqlServer()