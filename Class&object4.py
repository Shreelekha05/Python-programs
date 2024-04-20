class card:
    def __init__(self, pimageUrl, pdeviceType, pprice, prating):
        self.imageUrl = pimageUrl
        self.deviceType = pdeviceType
        self.price = pprice
        self.rating = prating

    def printalldetails(self):

        print("imageUrl:", self.imageUrl)
        print("deviceType:", self.deviceType)
        print("price:", self.price)
        print("rating:", self.rating)
        print()



m = card("Dummy-url 1", "Mobile", 56000, 4.5)
print("Product-1:")
m.printalldetails()

l = card("Dummy-url 2", "Laptop", 94000, 4.8)
print("Product-2:")
l.printalldetails()

s = card("Dummy-url 3", "Smart-watch", 18000, 3.5)
print("Product-3:")
s.printalldetails()


#########
target=int(input())
g=[1,10,22,3,4]
n=len(g)

for i in range(n):
    if target==g[i]:
        print("Target is present at index:",i)
        break
else:
    print("Target is not present")
