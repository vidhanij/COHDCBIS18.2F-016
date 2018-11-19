import pymongo
client =pymongo.mongoClient("mongodb://localhost:27017/")
db=client["ABCD_Company"]
collection=db["Users"]

print (".... User Login System .... ")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    UserName = input("Enter the Username please : ")
    UserId = input("Enter the User Id please : ")
    UserCategory = input("Enter the User Category please : ")
    UserPassword = input("Enter the Password please : ")
    for x in collection.find({},{"UserName":1,"UserId":1,"UserCategory":1,"UserPassword":1}):
        username=str (x["UserName"])
        userid=str(["UserId"])
        usercategory=str (x["UserCategory"])
        userPassword=str (x["UserPassword"])

    if(UserName=='username' and UserId == 'userid' and UserCategory == 'usercategory' and UserPassword == 'userPassword@'):
        print ("Logged In Successfully !!!")
        break
    else:
        print (" Invalid Credentials !!")
    
