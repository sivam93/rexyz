import psycopg2

connection = psycopg2.connect(user = "oikmebkezwdoyo",
                                  password = "8064557ebbd2142f12acd24a592779afe40c5d2f281c7c3148b48e4fe06971a6",
                                  host = "ec2-54-83-192-245.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "dfibjhnrqgjgam")
try:

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
