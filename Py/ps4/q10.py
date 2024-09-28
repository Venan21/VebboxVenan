def splitinto(gs,width):
    leng=len(gs)
    for i in range(0,leng,width):
        print(gs[i:i+4],"\n")






p="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w=4
splitinto(p,w)
    
