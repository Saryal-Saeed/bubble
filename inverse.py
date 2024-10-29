def inversal(num):
    size=len(num)
    for i in range(size//2):
        num[i],num[size-i-1]=num[size-i-1],num[i]
    return num 

num=[1,4,5,6,3]
print(inversal(num))