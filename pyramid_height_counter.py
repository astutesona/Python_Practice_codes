box=int(input("Enter number of boxes: "))
block=1
height=0
while box>=block:
     box=box-block
     height=height+1
     block+=1
print("The total height of the pyramid :",height)
