Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p_set = set(p)
    ans = 0
    for i in range(102):
        if i not in p_set:
            if abs(x - i) < abs(x - ans):
                ans = i
    print(ans)

=======
Suggestion 2

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    if n == 0:
        print(x)
    else:
        for i in range(100):
            if x-i not in p:
                print(x-i)
                break
            if x+i not in p:
                print(x+i)
                break

=======
Suggestion 3

def find_near_num(x, p_list):
    near_num = 0
    near_num_diff = 100
    for i in range(0, 101):
        if i in p_list:
            continue
        if abs(x - i) < near_num_diff:
            near_num_diff = abs(x - i)
            near_num = i
    return near_num

=======
Suggestion 4

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))

    if n == 0:
        print(x)
        return

    for i in range(100):
        if x - i not in p:
            print(x - i)
            return

        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 5

def find_nearest_value(x, p_list):
    """找到列表p_list中最接近x的值"""
    p_list.sort()
    if x < p_list[0]:
        return p_list[0]
    elif x > p_list[-1]:
        return p_list[-1]
    else:
        for i in range(len(p_list)):
            if x < p_list[i]:
                if x - p_list[i - 1] < p_list[i] - x:
                    return p_list[i - 1]
                else:
                    return p_list[i]
            elif x == p_list[i]:
                return x

=======
Suggestion 6

def find_closest_num(target, num_list):
    num_list.sort()
    if target <= num_list[0]:
        return num_list[0]
    if target >= num_list[-1]:
        return num_list[-1]
    for i in range(len(num_list)-1):
        if num_list[i] <= target <= num_list[i+1]:
            return num_list[i] if abs(num_list[i]-target) <= abs(num_list[i+1]-target) else num_list[i+1]

=======
Suggestion 7

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
    else:
        p = list(map(int, input().split()))
        p.sort()
        i = 0
        j = 0
        while i < len(p):
            if p[i] == x:
                p.pop(i)
                i -= 1
            i += 1
        while True:
            if x - j not in p:
                print(x - j)
                break
            elif x + j not in p:
                print(x + j)
                break
            j += 1

=======
Suggestion 8

def main():
    #print("请输入X和N")
    x,n = map(int,input().split())
    #print("请输入p1到pN")
    p = list(map(int,input().split()))
    p.append(x)
    p.sort()
    #print(p)
    for i in range(len(p)):
        if p[i] == x:
            print(p[i+1])
            break

=======
Suggestion 9

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        exit()
    for i in range(101):
        if x - i not in p:
            print(x - i)
            exit()
        elif x + i not in p:
            print(x + i)
            exit()

=======
Suggestion 10

def get_input():
    return input()
