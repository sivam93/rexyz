import psycopg2
import datetime
connection = psycopg2.connect(user = "ukqqsbqnvaclem",
                              password = "b2562d06904be9a723b69555b4ec73ee010736afd2f8b2500151b7448d4bbb15",
                              host = "ec2-54-197-239-115.compute-1.amazonaws.com",
                              port = "5432",
                              database = "d5lotqbh41te44")
cursor = connection.cursor()
def DatabaseSelectUser(name):
    #try:
        #Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        #cursor.execute("SELECT version();")
        #cursor.execute("CREATE TABLE account(user_id serial PRIMARY KEY,username VARCHAR (50) UNIQUE NOT NULL,password VARCHAR (50) NOT NULL,email VARCHAR (355) UNIQUE NOT NULL,created_on TIMESTAMP NOT NULL,last_login TIMESTAMP);")
        #cursor.execute("INSERT into account (user_id,username,password,email,created_on) values(01,'sss','sss','sss@gmail.com',' 2008-02-26 02:05:09');")
        #cursor.execute("SELECT * from account ;")
        Query="SELECT password from account where username=%s"
        #name=input()
        #print(name)
        cursor.execute(Query,(name,))
        #connection.commit()
        record = cursor.fetchone()
        return record
    #except (Exception, psycopg2.Error) as error :
        #print ("Error while connecting to PostgreSQL", error)
    


def DatabaseInsert():
    try:
        quer="INSERT into account (user_id,username,password,email,created_on) values(05,%s,%s,%s,%s);"
        cursor.execute(quer,(input(),input(),input(),str(datetime.datetime.now())))
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
