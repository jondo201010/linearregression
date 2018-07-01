#sum([pow(prefs[person1][item]-prefs[person2][item],2)for item in prefs[person1] if item in prefs[person2]])



def TestArrayExpression():
    arr=[1,2,3,4,5,6,7,8,9,11]
    x=(it*2 for it in arr if it%2==0)
    print(*x)
    print(arr)


def CreationOfDictionaryThroughFor():
    names=['Abcd','Batcher','Clone','Damascas','Eiffel']
    x=((name,name.lower()) for name in names)
    print(*x)

#--- Main Execution
TestArrayExpression()
CreationOfDictionaryThroughFor()