from random import *

new_path = 'itemPurchases.txt'
f= open(new_path,'w')
products={"22":"coffee","23":"cheeses","20":"eggs","21":"milk","1":"juice","2":"soda","3":"butter","4":"toilet paper","5":"hand soap","6":"shaving cream","7":"sandwich bags","8":"soap","9":"shampoo","10":"beef","11":"sugar","12":"flour","13":"waffles","14":" dinner rolls","15":"pasta","16":"ice cream","17":"dishwashing liquid","18":"paper towels","19":"batteries","24":"greeting cards","25":"juice","26":"sandwich loaves","27":"Pizza bar","28":"Rice","29":"Coconut Oil","30":"Bread","31":"Nuts"}


for u in range(0,10): 
        userID=str(randint(1, 9))
        ID=200+u   
	transactionID=str(ID+randint(1,200))
	for t in range(0,randint(1,10)):   #product to purchase in one transaction
        	purchaseAmount=str(randint(1,10))
        	product=randint(0,len(products)-1)
        	productName=products.values()[product]
 		productID=products.keys()[product]
		f.write(transactionID+"\t"+userID+"\t"+productID+"\t"+productName+"\t"+purchaseAmount+"\n")

