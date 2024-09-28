lst1 = [-5, 3, 6, 12, 15]
lst2 = [-12, -10, -6, -3, 4, 10]
#lst1.extend(lst2)
#lst1+lst2
for ele in lst2:
    lst1.append(ele)
lst1.sort()
n=len(lst1)
nby2=int(n/2);
if(n%2==0):
        median=(lst1[nby2]+lst1[nby2+1])/2
else: 
    median=lst1[nby2+1]/2
print(lst1)
print("median",median)
