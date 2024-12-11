import psycopg2
import pandas as pd

db_params = {
}

try:
    conn = psycopg2.connect(**db_params)
    print("connected to the database successfully")
except Exception as e:
    print(f"Error connecting to the database:{e}")
    exit()

cur = conn.cursor()

sql_query = "SELECT * FROM public.sch_locations";

try: 
    cur.execute(sql_query)
    rows = cur.fetchall()
except Exception as e:
    print(f"Error executing query: {e}")
    exit()

col_names = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows,columns=col_names)
df.to_csv('chat_history.csv',index=False)

df