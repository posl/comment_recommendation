Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] % 200
        C[i] = i + 1
    print("Yes")
    print(N)
    print(*C)
    print(N)
    print(*B)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        b[i] = a[i] % 200
    for i in range(n):
        c[i] = b[i] % 200
    b.sort()
    c.sort()
    if b[0] != b[1]:
        print("Yes")
        print("2")
        print("1", "2")
        print("1", "1")
    else:
        print("Yes")
        print("1")
        print("1")
        print("2")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        B.append(A[i] % 200)
    for i in range(N):
        C.append(A[i] % 200)
    for i in range(N):
        for j in range(i+1,N):
            if B[i] == B[j]:
                print("Yes")
                print(2)
                print(i+1,j+1)
                print(1)
                print(i+1)
                return 0
            if C[i] == C[j]:
                print("Yes")
                print(1)
                print(i+1)
                print(2)
                print(i+1,j+1)
                return 0
    print("No")
    return 0

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i]%200)
    c = []
    for i in range(n):
        c.append(i)
    d = dict()
    for i in range(n):
        if b[i] in d:
            d[b[i]].append(c[i])
        else:
            d[b[i]] = [c[i]]
    for i in range(200):
        if len(d[i])>=2:
            print('Yes')
            print(len(d[i]),end=' ')
            for j in range(len(d[i])):
                print(d[i][j]+1,end=' ')
            print()
            print(len(d[i]),end=' ')
            for j in range(len(d[i])):
                print(d[i][j]+1,end=' ')
            print()
            return
    print('No')

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    modA = [a % 200 for a in A]
    modA_dict = {}
    for i, a in enumerate(modA):
        if a in modA_dict:
            modA_dict[a].append(i+1)
        else:
            modA_dict[a] = [i+1]
    for key in modA_dict:
        if len(modA_dict[key]) > 1:
            print("Yes")
            print(len(modA_dict[key]))
            print(" ".join([str(x) for x in modA_dict[key]]))
            print(len(modA_dict[key]))
            print(" ".join([str(x) for x in modA_dict[key]]))
            return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    #print(A)
    memo = {}
    for i in range(2 ** N):
        b = []
        c = []
        for j in range(N):
            if (i >> j) & 1:
                b.append(j + 1)
            else:
                c.append(j + 1)
        #print(b, c)
        if len(b) == 0 or len(c) == 0:
            continue
        sum_b = sum([A[i] for i in b])
        sum_c = sum([A[i] for i in c])
        if sum_b % 200 == sum_c % 200:
            print("Yes")
            print(len(b), *b)
            print(len(c), *c)
            return
        if sum_b % 200 in memo:
            print("Yes")
            print(len(b), *b)
            print(len(memo[sum_b % 200]), *memo[sum_b % 200])
            return
        memo[sum_b % 200] = b
    print("No")

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mod = 200
    mod_a = [x % mod for x in a]
    d = {}
    for i, x in enumerate(mod_a):
        if x not in d:
            d[x] = [i]
        else:
            d[x].append(i)

    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(1, v[0] + 1)
            print(1, v[1] + 1)
            return

    for i in range(mod):
        for j in range(i + 1, mod):
            if i in d and j in d:
                print('Yes')
                print(1, d[i][0] + 1)
                print(2, d[i][1] + 1, d[j][0] + 1)
                return

    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    #print(modA)
    modAtoIndex = [[] for _ in range(mod)]
    for i in range(N):
        modAtoIndex[modA[i]].append(i)
    #print(modAtoIndex)
    for i in range(mod):
        if len(modAtoIndex[i]) >= 2:
            print("Yes")
            print(1, modAtoIndex[i][0] + 1)
            print(1, modAtoIndex[i][1] + 1)
            return
    for i in range(mod):
        for j in range(i + 1, mod):
            if len(modAtoIndex[i]) >= 1 and len(modAtoIndex[j]) >= 1:
                print("Yes")
                print(2, modAtoIndex[i][0] + 1, modAtoIndex[j][0] + 1)
                print(1, modAtoIndex[i][0] + 1)
                return
    print("No")
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割ったあまりの値をキーにして、その値が出現する位置をリストで保持する
    # あまりが0の場合は、その値が2回以上出現することはないので、
    # その場合は出現位置のリストの長さが2以上の場合に処理を行う
    # あまりが0以外の場合は、その値が2回以上出現することがあるので、
    # その場合は出現位置のリストの長さが1以上の場合に処理を行う
    mod = {}
    for i in range(N):
        m = A[i] % 200
        if m == 0:
            if m in mod and len(mod[m]) > 1:
                print('Yes')
                print(1, mod[m][0] + 1)
                print(1, mod[m][1] + 1)
                return
        else:
            if m in mod and len(mod[m]) > 0:
                print('Yes')
                print(1, mod[m][0] + 1)
                print(i + 1, end=' ')
                for j in range(N):
                    if j == mod[m][0]:
                        continue
                    print(j + 1, end=' ')
                print('')
                return
        if m in mod:
            mod[m].append(i)
        else:
            mod[m] = [i]
    print('No')

=======
Suggestion 10

def   solve ( N ,   A ): 
     # Implement this function 
     return   "No" ,   [] 

 # Don't edit below this line
