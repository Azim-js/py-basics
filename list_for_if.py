def prt_only_data(value):
    new_lst=[x for x in value if x>0]
    return new_lst
lst=[]
i=0
while i<=5:
    ele=int(input("enter the data : "))
    lst.append(ele)
    i=i+1
print(lst)
print("the data entered are : ",prt_only_data(lst))


def prnt_zero(val):
    return [x if not isinstance(x,str) else 0 for x in val]

a=[99,'nodata','nodata',0,5,29]
print("the list: ",prnt_zero(a))
