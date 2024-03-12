#Dictionary

mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
print(mydict)

#length
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
print(len(mydict))

#type
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
print(type(mydict))

#empty
mydict3={"name":"Anu",
        "Age":31,
        "year":1992}

#accessing
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
print(mydict["name"])



#for loop keys
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
for x in mydict:
    print("values :",x)

#for loop values
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
for x in mydict.values():
    print(x)

#clear
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
mydict.clear()
print(mydict)

#copy
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
mydict1=mydict.copy()
print(mydict1)

#pop
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
print(mydict.pop("Age"))

#pop item
mydict={"name":"Fasna",
        "Age":31,
        "year":1992}
x=mydict.popitem()
print(x)






