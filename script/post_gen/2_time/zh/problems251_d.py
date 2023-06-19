Synthesizing 8/10 solutions

=======
Suggestion 1

def get_all_weight(w):
    if w <= 3:
        return [w]
    if w <= 6:
        return [1, w-1]
    if w <= 9:
        return [2, w-2]
    if w <= 12:
        return [3, w-3]
    if w <= 15:
        return [1, 2, w-3]
    if w <= 18:
        return [1, 3, w-4]
    if w <= 21:
        return [2, 3, w-5]
    return [1, 2, 3, w-6]

=======
Suggestion 2

def solve(w):
    if w <= 3:
        print(3)
        print('1 2 3')
        return

    if w % 2 == 0:
        print(4)
        print('1 2 4 ' + str(w - 7))
        return

    print(5)
    print('1 2 4 ' + str(w - 7) + ' 7')

=======
Suggestion 3

def weight(w):
    if w == 3:
        return [1, 2, 3]
    elif w == 4:
        return [1, 2, 4]
    elif w == 5:
        return [1, 2, 5]
    elif w == 6:
        return [1, 2, 3, 6]
    elif w == 7:
        return [1, 2, 3, 7]
    elif w == 8:
        return [1, 2, 3, 4, 8]
    elif w == 9:
        return [1, 2, 3, 4, 9]
    elif w == 10:
        return [1, 2, 3, 4, 5, 10]
    elif w == 11:
        return [1, 2, 3, 4, 5, 11]
    elif w == 12:
        return [1, 2, 3, 4, 5, 6, 12]
    elif w == 13:
        return [1, 2, 3, 4, 5, 6, 13]
    elif w == 14:
        return [1, 2, 3, 4, 5, 6, 7, 14]
    elif w == 15:
        return [1, 2, 3, 4, 5, 6, 7, 15]
    elif w == 16:
        return [1, 2, 3, 4, 5, 6, 7, 8, 16]
    elif w == 17:
        return [1, 2, 3, 4, 5, 6, 7, 8, 17]
    elif w == 18:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]
    elif w == 19:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 19]
    elif w == 20:
        return [1, 2, 3, 4, 5

=======
Suggestion 4

def main():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 2)
    elif w == 3:
        print(2)
        print(1, 2)
    elif w == 4:
        print(3)
        print(1, 2, 4)
    elif w == 5:
        print(3)
        print(1, 2, 4)
    elif w == 6:
        print(3)
        print(1, 2, 3)
    else:
        print(6)
        print(1, 2, 3, 4, 5, 6)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def solve(w):
    if w <= 3:
        return [1, 2, 3][:w]
    else:
        ans = [1, 2, 3]
        if w % 2 == 0:
            ans.append(2)
        else:
            ans.append(3)
        if w % 2 == 0:
            for i in range(w // 4 - 1):
                ans.extend([4, 5])
            if w % 4 == 2:
                ans.append(4)
        else:
            for i in range(w // 4 - 1):
                ans.extend([4, 5])
            ans.append(6)
        return ans

=======
Suggestion 7

def main():
    print("hello world!")
    w = int(input())
    n = 6
    a = [1,2,3,4,5,6]
    print(n)
    print(a[0],a[1],a[2],a[3],a[4],a[5])

=======
Suggestion 8

def solve():
    w = int(input())
    if w <= 3:
        print(1)
        print(w)
    elif w <= 5:
        print(2)
        print(2, w - 2)
    else:
        print(3)
        print(2, 3, w - 5)
