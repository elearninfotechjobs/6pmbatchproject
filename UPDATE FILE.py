class product:
    def __init__(self,a=None, b=None, c=None):
        if (a!=None and b!=None and c!=None):
            print(a+b+c)
        elif (a!=None and b!=None):
            print(a-b)
obj=product(1,2)

