coffee=[["Coffee","Water","Milk","Icecream"],
        ["Espresso","No","No","No"],
        ["Long Black","Yes","No","No"],
        ["Flat White","No","Yes","No"],
        ["Cappuccino","No","Yes","No"],
        ["Affogato","No","No","Yes"]]

coffee2=coffee[1:]

for i in coffee2:
    if i[2].upper()=="YES":
        print len(i[2])

print float(len(i[2]))/float(len(coffee2))