import json
import uuid as idGen

class Order:
    def __init__(self):
        self.orderItems = []
        self.orders = []
        self.transportId = 0
        self.shipId = 0
        

    def addNewProduct(self):

        productId = self.idGenerator()
        productName = input("Write the product name: ")
        
        # Dictionary structure

        item = {
            # The str(productId) unserialize the UUID code
            "id" : str(productId), 
            "name" : productName
            }
        self.orderItems.append(item)

        # -------------------- #

    def closeOrder(self):

        if (len(self.orderItems) <= 0):
            print('No item was provided. Please enter one')
            return

        self.transportId = self.transportId + 1
        self.shipId = self.shipId + 1

        _orderItems = self.orderItems.copy()

        # Dictionary structure

        item = {
            "products" : _orderItems,
            "transportId" : self.transportId,
            "shipId" : self.shipId
        }
        
        self.orders.append(item)
        self.orderItems.clear()
        print("Your order was created")
        print('-----------------')

        # -------------------- #

    def documentOrders(self):

        if (len(self.orders) > 0): 
            with open("Orders.txt", "w") as outfile:
                json.dump(self.orders, outfile)
        else:
            print('The order has no items. Please enter at least one')
            self.newInput()

    def newInput(self): 

        userInput = str(input('Please enter N for adding a new order / product into the order, C for close the order or E for ending the transaction: '))

        if (userInput == "N"): 
            self.addNewProduct()
            self.newInput()
        elif (userInput == "C"):
            self.closeOrder()
            self.newInput()
        elif (userInput == "E"): 
            self.documentOrders()
        else: 
            self.newInput()

    def idGenerator(self):
        newId = idGen.uuid4()
        return newId