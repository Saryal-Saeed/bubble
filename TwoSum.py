def TwoSum(num, target):
    for i in range(len(num)):
        for j in range (i+1, len(num)):
            if num[i]+num[j]==target:
                return [i,j]
    return num



def TwooSum(num,target):
    data={}
    for i, nums in enumerate(num):
        sub=target-nums
        if sub in data:
            return [data[sub],i]
        data[nums]=i
    

numbers=[1,4,6,2,7,8]
TwooSum(numbers,10)