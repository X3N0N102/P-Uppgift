l1 = [1,0,0,0]
l2 = [0,1,0,0]
#l3 = [0,0,1,0]
#l4 = [0,0,0,1]
for i in range(0,3):
    if l1[i] == l2[i+1] and sum(l1+l2) > 1:
        print ("fel")
    else:
        print("rätt")



