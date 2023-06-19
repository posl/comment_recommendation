Synthesizing 10/10 solutions

=======
Suggestion 1

def find_closest_num(target, nums):
    nums.sort()
    min_diff = float('inf')
    closest_num = None
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if abs(nums[i] - target) < min_diff:
            min_diff = abs(nums[i] - target)
            closest_num = nums[i]
    return closest_num

=======
Suggestion 2

def find_nearest(x, p_list):
    if(len(p_list) == 0):
        return x
    p_list.sort()
    for i in range(len(p_list)):
        if(p_list[i] >= x):
            if(i == 0):
                return p_list[i]
            else:
                return find_nearest(x, [p_list[i-1], p_list[i]])
    return p_list[len(p_list)-1]

=======
Suggestion 3

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 4

def find_closest_int(x, list_int):
    # x: integer
    # list_int: list of integers
    # return: integer
    # find the closest integer to x in list_int
    # if there are two integers with same distance to x, return the smaller one
    # if list_int is empty, return x
    if len(list_int) == 0:
        return x
    else:
        list_int = sorted(list_int)
        min_distance = abs(x - list_int[0])
        closest_int = list_int[0]
        for i in list_int:
            if abs(x - i) < min_distance:
                min_distance = abs(x - i)
                closest_int = i
        return closest_int

=======
Suggestion 5

def main():
    x, n = map(int, raw_input().split())
    p = map(int, raw_input().split())
    if n == 0:
        print x
        return
    p.sort()
    if x not in p:
        print x
        return
    for i in range(100):
        if x - i not in p:
            print x - i
            return
        if x + i not in p:
            print x + i
            return

=======
Suggestion 6

def main():
    x,n = map(int, input().split())
    p = list(map(int, input().split()))
    p.append(x)
    p.sort()
    for i in range(101):
        if i not in p:
            break
    print(i)

=======
Suggestion 7

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = [int(i) for i in input().split()]
    for i in range(0, 100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 8

def get_closest_num(x, num_list):
    if len(num_list) == 0:
        return x
    else:
        min_diff = 100
        for num in num_list:
            if abs(num-x) < min_diff:
                min_diff = abs(num-x)
                closest_num = num
        return closest_num

=======
Suggestion 9

def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        exit()
    p = list(map(int,input().split()))
    num = 0
    for i in range(1,101):
        if i not in p:
            if abs(x-i) < abs(x-num):
                num = i
    print(num)

=======
Suggestion 10

def find_closest_num(num, arr):
    arr.sort()
    # print(arr)
    if num < arr[0]:
        return arr[0]
    if num > arr[-1]:
        return arr[-1]

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    if arr[low] - num < num - arr[high]:
        return arr[low]
    else:
        return arr[high]
