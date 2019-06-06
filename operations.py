import hello
import database
import psycopg2

def operationsUsernameCheck(user):  
     try:
         userName=database.DatabaseSelectUser(user)
         if userName[0] is None:
              return False
         else:
              return True
     except (Exception, psycopg2.Error) as error :
          print(error)
          return False


def operationsPasswordCheck(user,password):
     try:
         passwordfromdb=database.DatabaseSelectUser(user)
         if(password==passwordfromdb[0]):
              return True
         else:
              return False
     except (Exception, psycopg2.Error) as error :
          return False



