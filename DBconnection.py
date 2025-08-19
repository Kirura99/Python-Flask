import sqlite3

databaseName = "C:/ProgrammingStudy/JAVA/Pyton/Flask2Product/product.db"


def delleteRequest(id):
   query = "Delete from Alcohol where id = "+str(id)+";" 
   try:
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
   except Exception as e:
        print(e.__str__()) 



def addNewAlcohol(name, img_url, degree, price, isDiscount):
    query = """
    INSERT INTO Alcohol(name, img_url, degree, price, discount)
    VALUES (?, ?, ?, ?, ?)
    """
    try:
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(query, (name, img_url, degree, price, isDiscount))
        connection.commit()
        connection.close()
    except Exception as e:
        print(e.__str__())    
        
        
#addNewAlcohol("Cocacola", " ...",12,1.56,0)        
        

def getData(query):
    try:
        connection = sqlite3.Connection(databaseName)
        cursor=connection.cursor()
        
        cursor.execute(query)
        data = cursor.fetchall()
        
        connection.close()
        
        print(data)
        return data
    except Exception as e:
        print(e.__str__())    
        
query = "SELECT * FROM Alcohol ORDER by	name;"  
getData(query)      