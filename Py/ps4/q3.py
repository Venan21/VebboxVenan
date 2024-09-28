lst=[100,31, 13, 97, 10, 20, 11]
leng=len(lst)
for i in range(1,leng):
    if((lst[i-1]<lst[i])and(lst[i+1]<lst[i])):
        print(lst[i])
        break
