lst= [50,3,10,7,40,80];
#[10,9,2,5,3,7,101,18]
subli=[];
def subseqAS(li,index):
    sub=[]
    lenofli=len(li)
    sub.append(li[index]);
    for i in range(index,lenofli-1):
        #print(i,"th iteration")
        #print(" i",li[i],li[i+1])
        if(li[i+1]>li[i]):

            sub.append(li[i+1])
    print(sub)
    return sub
#print(subseqAS(lst,0))
lenofsub=[];
longest=0;
for i in range(0,len(lst)):
    a=subseqAS(lst,i)
    subli.append(a);
    lenofsub.append(len(a))
    if(lenofsub[i]>longest):
        longest=lenofsub[i]
    
print(longest)


