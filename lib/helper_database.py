from pandas import DataFrame
import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
import random

THIS_HOST='54.200.77.93'
THIS_USER='postgres'
THIS_PASSWORD='postgres'
COUNT = 220000

def _con_cur_query(query):
    con = pg2.connect(host=THIS_HOST, 
                        user=THIS_USER,
                        password=THIS_PASSWORD)
    cur = con.cursor(cursor_factory=RealDictCursor)
    cur.execute(query)
    results = DataFrame(cur.fetchall())
    con.close()
    return results


def _generate_random_yodas_string(count = COUNT,n = 220,seed=None):
    if seed:
        random.seed(seed)
    my_list = random.sample(range(count),n)
    my_string_list = [str(i) for i in my_list]
    
    return ','.join(my_string_list)


def _generate_table_group(table_group):
    table_groups = {
    'A':['madelon_data_1','madelon_data_2'],
    'B':['madelon_data_3','madelon_data_4'],
    'C':['madelon_data_5','madelon_data_6'],
    'D':['madelon_data_7','madelon_data_8'],
    }
    return table_groups[table_group]

	
def query_tables(yodas, table_group):
    table_1, table_2 = _generate_table_group(table_group)
    query = """
        select * 
        from {} as m1 
        join {} as m2
        on m1.yoda = m2.yoda
        where m1.yoda in ({});
    """.format(table_1, table_2, yodas)
 
    return _con_cur_query(query)


def query_target_table(yodas):
    query = """
        select * 
        from madelon_target
        where madelon_target.yoda in ({});
    """.format(yodas)

    return _con_cur_query(query)

def make_DataFrame(count=COUNT, n=220, drop_cols=None, seed=None):    
    these_yodas = _generate_random_yodas_string(count=count, 
                                                n=n,
                                                seed=seed)
    
    feature_A = query_tables(these_yodas,'A')
    feature_B = query_tables(these_yodas,'B')
    feature_C = query_tables(these_yodas,'C')
    feature_D = query_tables(these_yodas,'D')
    feature = (feature_A.merge(feature_B, on='yoda')
                        .merge(feature_C, on='yoda')
                        .merge(feature_D, on='yoda'))
    feature.set_index('yoda', inplace = True)
    
    if drop_cols:
        feature.drop(drop_cols, axis=1,inplace=True)

    target = query_target_table(these_yodas)
    target.set_index('yoda', inplace = True)
    return feature, target


def query_verification():
    query = """select * from madelon_data_1 limit 1;"""
  
    return _con_cur_query(query)




