for row in range(6):
    for col in range(5):
        # if(row-col==0 and (row!=3 and row!=4)) or (row+col==4 and (row!=3 and row!=4)) or (col==2 and (row!=0 and row!=1)):
        if((col==0 or col==4) and (row!=2 and row!=3 and row!=4 and row!=5)) or (row==2 and (col!=0 and col!=2 and col!=4)) or (col==2 and (row!=0 and row!=1 and row!=2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()