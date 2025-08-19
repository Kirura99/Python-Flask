from flask import Flask
from flask import render_template
from DBconnection import getData, addNewAlcohol,delleteRequest
from flask import request
from flask import redirect



webPage = Flask(__name__)


@webPage.route("/alchocol",methods=['POST','GET'])
def alchocol():
    query = "SELECT * FROM Alcohol ORDER by	name;"
    
    if request.method =="POST":
        if request.form.__contains__("drinkID"):
            drinkToDellete = request.form["drinkID"]
            delleteRequest(drinkToDellete)
        
        if request.form.__contains__("find"):
            print("Drink to find", request.form["find"])
            query=" Select * from Alcohol where name like '%"+request.form["find"]+"%';"
        
          
        
    alcoData = getData(query)
    return render_template(template_name_or_list="alchocol.html",alcoData=alcoData)



@webPage.route("/alcohol/<int:id>")
def oneAlcohol(id):
    query = "Select * from Alcohol where id ="+str(id)+";" 
    oneDrink = getData(query)[0]
    return render_template("one_alcohol.html", oneDrink =oneDrink)
    oneDrink = getData(query)
    

    
    
@webPage.route("/add_alcohol", methods=['POST', 'GET']) 
def add_alcohol():
    if request.method =="POST":
        print("Add new drink!!")
        
        newAlcoName = request.form.get("name")
        newAlcoUrl = request.form.get("img_url")
        newAlcoDgr = request.form.get("degree")
        newAlcPrice = request.form.get("price")
        #newAlcDiscount = request.form["discount"]
        #print(newAlcoName+" "+newAlcoDgr+" "+newAlcPrice+" "+newAlcoUrl)
        
        
        isDiscount = 0
        if request.form.__contains__("discount"):
            isDiscount=1
            addNewAlcohol(newAlcoName,newAlcoUrl,newAlcoDgr,newAlcPrice,isDiscount)
        return redirect("/")
    else:    
        return render_template("add_alcohol.html")

@webPage.route("/")
def mainRoot():
    return render_template("index.html")

@webPage.route("/all_users")    
def allUsers():
    

    query = "Select * from Users order by name;" 
    #oneDrink = getData(query)
    #return render_template("all_users.html", oneUser =oneUser)
    #oneDrink = getData(query)
    userData = getData(query)
    return render_template(template_name_or_list="all_users.html",userData=userData)



@webPage.route("/log_in")
def logIn():
    return render_template("log_in.html")




if __name__ == "__main__":
    webPage.run(debug=True)
    
    

