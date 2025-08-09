
arr=[1,2,3,4,5,6]
total =0
for num in arr:
    total+=1
print( 'total',num)

arr=[22,3,4,1,111]
max_num=arr[0]
for num in arr:
    if num >max_num:
        max_num=num
print('maxmimum number is',max_num)

#Reverse Array – Python
arr=[3,4,5,61,2]
revers_arr=arr[::-1]


print(revers_arr)

arr=[3,4,5,61,2]
print(arr[5:1:-2])
print(arr[3:0:-1])
print(arr[:])
print(arr[::-2])
print(arr[1:4:1])