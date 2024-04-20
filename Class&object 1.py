#classes and objects
class Card:
    def __init__(self,imgurl,price,rating,descrip,deliverywithin,comments,brandname):
        self.imageurl=imgurl
        self.cost = price
        self.rate = rating
        self.des= descrip
        self.delivery=deliverywithin
        self.review=comments
        self.brand=brandname

#obj creation
laptop= Card("http.img",75000,4.5,"16GB RAM and 512GB ROM","2days",["nice","awesome features"],"DELL")
print(laptop.imageurl)
print(laptop.cost)
print(laptop.rate)
print(laptop.des)
print(laptop.delivery)
print(laptop.review)
print(laptop.brand)
print()

mobile=Card("http.img",14000,4.3,"4GB RAM  128GB ROM","5days",["good","awesome features"],"Redmi")
print(mobile.imageurl)
print(mobile.cost)
print(mobile.rate)
print(mobile.des)
print(mobile.delivery)
print(mobile.review)
print(mobile.brand)
print()

smartwatch=Card("http.img",3000,4.2,"2GB RAM and 16GB ROM","3days",["usable","awesome features"],"Boat")
print(smartwatch.imageurl)
print(smartwatch.cost)
print(smartwatch.rate)
print(smartwatch.des)
print(smartwatch.delivery)
print(smartwatch.review)
print(smartwatch.brand)
