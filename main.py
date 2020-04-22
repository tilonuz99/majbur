import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE grs
          (grid BIGINT,
          userid BIGINT,
          kanal LONGTEXT); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
