def SquaredValues(beg,end):
    lst=[]
    for i in range(beg,end):
        lst.append(i**2)

    lst_even=[]
    lst_odd=[]

    for i in lst:
        if i%2==0:
         lst_even.append(i)
        else:
         lst_odd.append(i)

        print("Here is a list of specified even numbers:",lst_even)
        print("Here is a list of specified odd numbers:",lst_odd)
beg=int(input("Enter starting range:"))
end=int(input("enter end range:"))
SquaredValues(beg,end)


