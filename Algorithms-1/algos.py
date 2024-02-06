# from random import randint
# from time import time

# def power(a, b):
#     if b == 0:
#         return 1, 0
#     elif b == 1:
#         return a, 0
#     elif b % 2 == 1:
#         x, cnt = power(a, b // 2)
#         return x * x * a, 2 + cnt
#     elif b % 2 == 0:
#         x, cnt = power(a, b // 2)
#         return x * x, 1 + cnt


# N  = [1, 10, 100, 10**3, 10**4, 10**5]
# for n in N:

#     arr = [randint(0, n) for i in range(n)]
#     start = time()
    
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]


#     end = time()

#     print(n, end - start)


# def mymin(arr):
#     mn = float('inf')
#     for i in arr:
#         if mn > i:
#             mn = i
#     return mn

# def mymax(arr):
#     mx = float('-inf')
#     for i in arr:
#         if mx < i:
#             mx = i
#     return mi

# print('min value in arr', mymax([1,2,3, 0]))



### - in an array of pairs find single
### https://leetcode.com/problems/single-number/description/
from random import randint
from time import time

N = 10**9

arr = [i for i in range(N)]
arr = arr + arr + [1000001]
start = time()

### SLOW version
# for i, val in enumerate(arr):
#     if val not in (arr[:i] + arr[i+1:]):
#         print(val)

### FAST version
x = 0
for i in arr:
    x = x ^ i
print(x)

end = time()
print('time: ', end - start)

