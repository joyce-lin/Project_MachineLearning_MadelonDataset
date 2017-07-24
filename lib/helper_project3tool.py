import psycopg2
from psycopg2.extras import RealDictCursor # return column name as key and result as value
import pandas as pd

class project3tool(object):
    
    def __init__(self,
                    COUNT = 220000,
                    HOST = '54.200.77.93',
                    PORT = 5432,
                    DATABASE ='postgres',
                    PASSWORD ='postgres',
                    USER ='postgres',
                    SEED = 42):
        
        self.COUNT = COUNT
        self.HOST = HOST
        self.PORT = PORT
        self.DATABASE = DATABASE
        self.PASSWORD = PASSWORD
        self.USER = USER
        self.SEED = SEED
        self.TABLE = {i:'madelon_data_{}'.format(i) for i in range(1,9)}
        self.POSITION = 0
        
    def make_query(self, table_name, yoda_list):
        yoda_list=','.join([str(yoda) for yoda in yoda_list])

        query='''
                SELECT * 
                FROM {}
                where {}.yoda in ({});

                '''.format(table_name,table_name, yoda_list)
    
        return query

    def query_table (self, table_name, yoda_list):
        query = self.make_query(table_name,yoda_list)
        con = psycopg2.connect(database=DATABASE, 
                               port=PORT,user=USER, 
                               password=PASSWORD,
                               host=HOST)
        
        cur=con.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        result = cur.fetchall()
        con.close()
        return pd.DataFrame(result).set_index(['yoda'])    


    def get_data(self, yodas):
        dfs=[]
        for table in range(1,9):
            dfs.append(self.query_table(TABLES[table],yodas))

        merged = pd.concat(dfs, axis=1)
        
        target= self.query_table('madelon_target',yodas)
        target = pd.DataFrame(target)
        
        return merged, target
    
    
    def load_sequential(self, n=100, position = None):
        if not position:
            pos = self.POSITION
        else:
            pos = position
        
        data, target = self.get_data(range(pos, pos+n))
        
        if not position:
            self.POSITION += n
            
        self.POSITION +=n
        
    
        return data, target
    
    def reset_position(self):
        self.POSITION = 0