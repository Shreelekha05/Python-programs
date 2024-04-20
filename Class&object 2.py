class Card:
    def __init__(self,imgurl,price,rating,descrip,deliverywithin,comments,brandname):
        self.imageurl=imgurl
        self.cost = price
        self.rate = rating
        self.des= descrip
        self.delivery=deliverywithin
        self.review=comments
        self.brand=brandname
    def alldetails(self):
        print(self.imageurl)
        print( self.cost)
        print(self.rate)
        print (self.des)
        print (self.delivery)
        print (self.review)
        print(self.brand)
        print()

laptop = Card("http.img", 75000, 4.5, "16GB RAM and 512GB ROM", "2days", ["nice", "awesome features"], "DELL")
laptop.alldetails()

mobile=Card("http.img",14000,4.3,"4GB RAM  128GB ROM","5days",["good","awesome features"],"Redmi")
mobile.alldetails()

smartwatch = Card("http.img", 3000, 4.2, "2GB RAM and 16GB ROM", "3days", ["usable", "awesome features"], "Boat")
smartwatch.alldetails()
