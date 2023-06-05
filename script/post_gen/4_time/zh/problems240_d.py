Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0]*n
    for i in range(n):
        b[i] = a[i]
        if i == 0:
            print(1)
            continue
        if a[i] == a[i-1]:
            b[i] = 0
        print(len(set(b))-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        if a[i] not in c:
            c[a[i]] = 1
        else:
            c[a[i]] += 1
    ans = 0
    for i in c:
        ans += c[i] - 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] -= 1
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [3, 2, 3, 2, 2]
    #a = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i]-1] += 1
    #print(b)
    for i in range(n):
        print(n - sum(b[0:a[i]]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [3, 2, 3, 2, 2]
    # A = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    B = [0] * 200001
    for a in A:
        B[a] += 1
    # print(B)
    ans = 0
    for i in range(200001):
        if B[i] > 0:
            ans += 1
            B[i] -= 1
        if B[i] > 0:
            B[i + 1] += B[i]
    print(ans)

=======
Suggestion 6

def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i]-1]+=1
    for i in range(n):
        if b[i]==0:
            print(0)
            continue
        elif b[i]==1:
            print(1)
            continue
        else:
            if b[i]%2==0:
                print(0)
            else:
                print(1)
main()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    result = []
    for i in range(n):
        if i == 0:
            result.append(1)
            continue
        if a[i] == 2:
            result.append(result[i-1])
        else:
            result.append(result[i-1]+1)
    #print(result)
    for i in range(n):
        print(result[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2

    # 2 3 2 3 3 3 2 3 3 2
    # 2 3 2 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2
    # 2 2 3 3 3 3 2 3 3 2

    # 2 3 2 3 3 3 2 3 3

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + 1
        if a[i] == a[i - 1]:
            b[i] = b[i - 1]
    for i in range(1, n + 1):
        print(b[i])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            ans[i+1] = ans[i]
    for i in range(n-1, 0, -1):
        if a[i] == a[i-1]:
            ans[i-1] = ans[i]
    for i in range(n):
        print(ans[i])
