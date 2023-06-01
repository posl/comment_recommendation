Synthesizing 10/10 solutions

=======
Suggestion 1

def find_nearest(x, p):
    #print("x: %d" % x)
    #print("p: %s" % p)
    if len(p) == 0:
        return x
    else:
        min = 100
        for i in p:
            if abs(x - i) < min:
                min = abs(x - i)
        return min + x

=======
Suggestion 2

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
    else:
        p.append(x)
        p.sort()
        index = p.index(x)
        if index == 0:
            print(p[1])
        elif index == n:
            print(p[n-1])
        else:
            if (p[index] - p[index-1]) > (p[index+1] - p[index]):
                print(p[index+1])
            else:
                print(p[index-1])

=======
Suggestion 3

def problem170_c():
    x = int(input().strip())
    n = int(input().strip())
    p = list(map(int,input().strip().split()))
    p.append(x)
    p.sort()
    for i in range(len(p)-1):
        if p[i] == x:
            if abs(p[i-1]-x) <= abs(p[i+1]-x):
                print(p[i-1])
            else:
                print(p[i+1])
            break

=======
Suggestion 4

def get_closest_number(x, p_list):
    closest_number = x
    diff = x
    for p in p_list:
        if abs(x - p) < diff:
            closest_number = p
            diff = abs(x - p)
    return closest_number

=======
Suggestion 5

def find_closest_num(array, num):
    if len(array) == 0:
        return num
    else:
        closest_num = array[0]
        for n in array:
            if abs(num-n) < abs(num-closest_num):
                closest_num = n
        return closest_num

input_str = input()
input_list = input_str.split()
x = int(input_list[0])
n = int(input_list[1])

=======
Suggestion 6

def find_min_diff(x, p):
    min_diff = 100
    for i in range(0, 101):
        if i not in p:
            if abs(x - i) < min_diff:
                min_diff = abs(x - i)
                result = i
    return result

=======
Suggestion 7

def find_nearest_int(x, n, p):
    min_diff = 100
    nearest_int = 0
    for i in range(1, 101):
        if i not in p:
            diff = abs(x - i)
            if diff < min_diff:
                min_diff = diff
                nearest_int = i
    return nearest_int

=======
Suggestion 8

def findClosestInt(x, p):
    p.sort()
    if x in p:
        return x
    if len(p) == 0:
        return x
    if x < p[0]:
        return p[0]
    if x > p[-1]:
        return p[-1]
    for i in range(len(p)):
        if x < p[i]:
            if p[i] - x < x - p[i-1]:
                return p[i]
            else:
                return p[i-1]

=======
Suggestion 9

def findClosestNumber(x, n, p):
    if n == 0:
        return x
    if x in p:
        return findClosestNumber(x + 1, n, p)
    else:
        return x

=======
Suggestion 10

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    ans = x
    for i in range(102):
        if i in p:
            continue
        if abs(x - i) < abs(x - ans):
            ans = i
    print(ans)
