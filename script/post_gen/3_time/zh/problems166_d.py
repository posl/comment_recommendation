Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(x):
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                return a,b
    return None

x = int(input())
a,b = solve(x)
print(a,b)

=======
Suggestion 2

def getAB(x):
    for a in range(100):
        for b in range(100):
            if a**5-b**5==x:
                return a,b
    return None

=======
Suggestion 3

def getAB(X):
    for A in range(0, 1000):
        for B in range(-1000, 1000):
            if A**5 - B**5 == X:
                return A, B
    return 0, 0

=======
Suggestion 4

def main():
    # 读取输入
    x = int(input())

    # 从-200到200遍历A
    for a in range(-200, 200):
        # 从-200到200遍历B
        for b in range(-200, 200):
            # 如果A的5次方-B的5次方等于X
            if a ** 5 - b ** 5 == x:
                # 输出A和B
                print(a, b)
                # 退出程序
                exit()

=======
Suggestion 5

def solve(x):
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                return a, b

x = int(input())
a, b = solve(x)
print(a, b)

=======
Suggestion 6

def findAB(X):
    for A in range(1, 1001):
        for B in range(-1000, 0):
            if A ** 5 - B ** 5 == X:
                return A, B

X = int(input())
A, B = findAB(X)
print(A, B)

=======
Suggestion 7

def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 8

def main():
    x = int(input())
    for a in range(-120,120):
        for b in range(-120,120):
            if pow(a,5) - pow(b,5) == x:
                print(a,b)
                return

=======
Suggestion 9

def main():
    x = int(input())
    for a in range(-118,120):
        for b in range(-119,119):
            if a**5 - b**5 == x:
                print(a,b)
                return
