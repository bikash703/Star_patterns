for row in range(7):
    for col in range(5):
        if(col==0) or (row-col==2) or (row+col==4):
            print("*",end="")
        else:
            print(end=" ")
    print()