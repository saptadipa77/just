from main import client,db_id,db_collection_id
from appwrite.services.databases import Databases
import secrets


db=Databases(client)


#result=db.create(
    #database_id=secrets.token_hex(8),
    #name= 'todos_db'
   # )


   #create a collection
#result=db.create_collection(
   # database_id=db_id,
   # collection_id=secrets.token_hex(8),
   # name='too'
#)

#define attributes
#result=db.create_string_attributes(
    #databases_id=db_id,
    #collection_id=db_collection_id,
   # key='title',
   # size=225
#)

#result=db.create_string_attributes(
    #databases_id=db_id,
   # collection_id=db_collection_id,
   # key='content',
   # size=225,
   # required=True
#)

#result=db.create_datetime_attribute(
   # database_id=db_id,
   # collection_id=db_collection_id,
   # key='date_added',
   # required=True
#)


#print(result)


class CRUD:
    def __init__(self):
        self.db_id=db_id,
        self.coll_id=db_collection_id
    def list_todos(self):
        result=db.list_documents(
        database_id=self.db_id,
        collection_id=self.coll_id
        )
        return result
    

def create_todo(self,data:dict):
    result=db.create_document(
        database_id=self.db_id,
        collection_id=self.coll_id,
        data=data
    )
    return result


def retrieve_todo(self,todo_id:)



    
