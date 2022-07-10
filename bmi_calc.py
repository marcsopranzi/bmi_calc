
from operator import index
from unicodedata import decimal
import pandas as pd
import sqlite3
import math 


bmi_path = 'data/table1.json'
category_path = 'data/catalog.csv'
conn = sqlite3.connect(":memory:")

def sqlite_power(x,n):
    return x**n

conn.create_function("power", 2, sqlite_power)

df_bmi_data = pd.read_json(bmi_path)
df_category_data = pd.read_csv(category_path, sep='\t')

df_bmi_data.to_sql("table_bmi_data", conn, index=False)
df_category_data.to_sql("table_category_data", conn, index=False)

qry_bmi_calculation = """select *, 
                                WeightKg/power(cast(HeightCm as real)/100, 2) as BMI_index 
                         from table_bmi_data"""

def bmi_calculation(df):
    df = pd.read_sql_query(qry_bmi_calculation,conn)
    return df

df_bmi_data_bmi = bmi_calculation(df_bmi_data)

df_bmi_data_bmi.to_sql("table_bmi_data_bmi", conn, index=False)

qry_bmi_categorization = """select Gender,
                                   HeightCm,
                                   WeightKg,
                                   bmi_category bmi_range_kg_m2,
                                   health_risk
                            from table_bmi_data_bmi 
                            join table_category_data on table_bmi_data_bmi.BMI_index > table_category_data.bmimin and 
                                 table_bmi_data_bmi.BMI_index <  table_category_data.bmimax"""

def bmi_categorization(df):
    df = pd.read_sql_query(qry_bmi_categorization, conn)
    return df

df_bmi_data_category = bmi_categorization(df_bmi_data_bmi)

print(df_bmi_data_category)
