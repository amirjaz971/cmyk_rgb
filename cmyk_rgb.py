from math import floor

def round(num):
    if num>floor(num)+0.5:
        return floor(num)+1
    elif num<=floor(num)+0.5:
        return floor(num)
    else:
        return num
rgb=''
rgb_lst=[]
c=float(input('enter the number representing cyan: '))
m=float(input('enter the number representing magenta: '))
y=float(input('enter the number representing yellow: '))
k=float(input('enter the number representing black: '))
R=255*(1-c)*(1-k)
G=255*(1-m)*(1-k)
B=255*(1-y)*(1-k)
counter=0
if 0<=c<1 and 0<=m<1 and 0<=y<1 and 0<=k<1:
    rgb_lst.append(R)
    rgb_lst.append(G)
    rgb_lst.append(B)
    for i in rgb_lst:
        counter+=1
        rgb+=str(round(i))
        if counter!=len(rgb_lst):
            rgb+=','
        
    print(rgb)    
else:
    print('out of range!')




