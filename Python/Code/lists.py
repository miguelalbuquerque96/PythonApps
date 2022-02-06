catNames=[]
while True:
    print('Enter a cat name'+str(len(catNames)+1)+' or nothing to break cicle.')
    
    name=input()
    
    if name =='':
        break
    catNames = catNames+ [name]

print('the cats names are')
for name in catNames: 
    print(name)
    

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print('pens' in supplies)