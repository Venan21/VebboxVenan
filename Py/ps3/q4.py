lst=[1,2,5,2,4,5,8,7]
le=len(lst)
half=int(le/2)
fsum=0;ssum=0;
for i in range(0,half):
    fsum+=lst[i]
for i in range(half,le):
    ssum+=lst[i]
if(fsum==ssum):
    print("balanced")
elif(fsum>ssum):
    print("add to left +",fsum-ssum)
elif(fsum<ssum):
    print("addto right side",ssum-fsum)
