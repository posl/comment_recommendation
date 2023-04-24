Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print('Yes')
                return
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print('Yes')
                    return
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print('Yes')
                        return
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print('Yes')
                            return
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print('Yes')
                                return
                            for o in range(1, 7):
                                if i + j + k + l + m + n + o == B and A == 7:
                                    print('Yes')
                                    return
                                for p in range(1, 7):
                                    if i + j + k + l + m + n + o + p == B and A == 8:
                                        print('Yes')
                                        return
                                    for q in range(1, 7):
                                        if i + j + k + l + m + n + o + p + q == B and A == 9:
                                            print('Yes')
                                            return
                                        for r in range(1, 7):
                                            if i + j + k + l + m + n + o + p + q + r == B and A == 10:
                                                print('Yes')
                                                return
                                            for s in range(1, 7):
                                                if i + j + k + l + m + n + o + p + q + r + s == B and A == 11:
                                                    print('Yes')
                                                    return
                                                for t in range(1, 7):
                                                    if i + j + k + l + m + n + o + p + q + r + s + t == B and A == 12:
                                                        print('Yes')
                                                        return
                                                    for u in range(1, 7):
                                                        if

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print("Yes")
                return
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print("Yes")
                    return
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print("Yes")
                        return
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print("Yes")
                            return
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print("Yes")
                                return
    print("No")
    return

=======
Suggestion 3

def main():
    A, B = map(int, input().split())

    for i in range(1, 7):
        for j in range(1, 7):
            if A == 2 and i + j == B:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A * 1 <= B <= A * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if B > 6 * A:
        print('No')
    elif B < A:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    elif 1 * A > B:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def dice(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if i+j==b and a==2:
                return 'Yes'
    return 'No'

a,b=map(int,input().split())
print(dice(a,b))

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    if A <= 6 and B <= 6:
        if A * 6 >= B:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    #入力
    A, B = map(int, input().split())
    #出力
    print("Yes" if A <= B <= A * 6 else "No")
