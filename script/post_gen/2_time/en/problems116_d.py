Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    # print(sushi)
    kinds = set()
    ans = 0
    for i in range(K):
        d, t = sushi[i]
        ans += d
        kinds.add(t)
    ans += len(kinds) ** 2
    # print(ans)
    for i in range(K, N):
        d, t = sushi[i]
        if len(kinds) == K:
            break
        if t in kinds:
            continue
        ans += d
        kinds.add(t)
        ans += 2 * len(kinds) - 1
        # print(ans)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append([d, t])
    Sushi.sort(reverse=True)
    Sushi = Sushi[:K]
    Sushi.sort(key=lambda x:x[1])
    Sushi2 = Sushi[:]
    Sushi2.sort()
    Sushi3 = Sushi[:]
    Sushi3.sort(key=lambda x:x[0], reverse=True)
    ans = 0
    for i in range(K):
        ans += Sushi[i][0]
    ans += (len(set(Sushi))**2)
    for i in range(K):
        if len(set(Sushi2)) == K:
            break
        if Sushi2[i][1] not in set(Sushi2[:i]):
            Sushi2.append(Sushi2[i])
            Sushi2.sort(key=lambda x:x[1])
            Sushi2.sort(key=lambda x:x[0], reverse=True)
            Sushi2 = Sushi2[:K]
            ans2 = 0
            for j in range(K):
                ans2 += Sushi2[j][0]
            ans2 += (len(set(Sushi2))**2)
            if ans2 > ans:
                ans = ans2
    for i in range(K):
        if len(set(Sushi3)) == K:
            break
        if Sushi3[i][1] not in set(Sushi3[:i]):
            Sushi3.append(Sushi3[i])
            Sushi3.sort(key=lambda x:x[1])
            Sushi3.sort(key=lambda x:x[0], reverse=True)
            Sushi3 = Sushi3[:K]
            ans3 = 0
            for j in range(K):
                ans3 += Sushi3[j][0]
            ans3 += (len(set(Sushi3))**2)
            if ans3 > ans:
                ans = ans3
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    kinds = set()
    total = 0
    for i in range(K):
        kinds.add(sushi[i][0])
        total += sushi[i][1]
    ans = len(kinds) ** 2 + total
    for i in range(K, N):
        if sushi[i][0] in kinds:
            continue
        kinds.add(sushi[i][0])
        total += sushi[i][1]
        for j in range(K):
            if sushi[j][0] in kinds:
                continue
            kinds.remove(sushi[j][0])
            total -= sushi[j][1]
            break
        ans = max(ans, len(kinds) ** 2 + total)
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    Sushi = []
    for i in range(N):
        t,d = map(int,input().split())
        Sushi.append((t,d))
    Sushi.sort(key=lambda x:x[1],reverse=True)
    #print(Sushi)
    Left = []
    Right = []
    Left_Topping = {}
    Right_Topping = {}
    Left_Topping[Sushi[0][0]] = 1
    Left.append(Sushi[0])
    Right_Topping[Sushi[-1][0]] = 1
    Right.append(Sushi[-1])
    for i in range(1,N):
        if not Sushi[i][0] in Left_Topping:
            Left_Topping[Sushi[i][0]] = 1
            Left.append(Sushi[i])
        if not Sushi[-i-1][0] in Right_Topping:
            Right_Topping[Sushi[-i-1][0]] = 1
            Right.append(Sushi[-i-1])
    #print(Left)
    #print(Right)
    Left_Total = 0
    Right_Total = 0
    for i in range(len(Left)):
        Left_Total += Left[i][1]
    for i in range(len(Right)):
        Right_Total += Right[i][1]
    #print(Left_Total)
    #print(Right_Total)
    if len(Left) == K:
        print(Left_Total + len(Left)**2)
        return
    if len(Left) == N:
        print(Left_Total + len(Left)**2)
        return
    if len(Right) == K:
        print(Right_Total + len(Right)**2)
        return
    if len(Right) == N:
        print(Right_Total + len(Right)**2)
        return
    Max = 0
    for i in range(len(Left)):
        for j in range(len(Right)):
            if Left[i][0] != Right[j][0]:
                if i+j+1 <= K:
                    if Max < Left_Total + Right_Total + (i+j+1)**2 - Left[i][1] - Right[j][1]:
                        Max = Left_Total + Right_Total + (i+j+1)**2 - Left[i][1] - Right[j][1]
    print(Max)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    Sushi = [list(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    s = 0
    variety = set()
    for i in range(K):
        s += Sushi[i][1]
        variety.add(Sushi[i][0])
    ans = s + len(variety) * len(variety)
    for i in range(K, N):
        if Sushi[i][0] in variety:
            continue
        else:
            variety.add(Sushi[i][0])
            for j in range(K):
                if Sushi[j][0] not in variety:
                    s = s - Sushi[j][1] + Sushi[i][1]
                    ans = max(ans, s + len(variety) * len(variety))
                    break
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    TD = [list(map(int, input().split())) for i in range(N)]
    TD.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    kinds = set()
    total = 0
    for i in range(K):
        kinds.add(TD[i][0])
        total += TD[i][1]
    ans = total + len(kinds) ** 2
    for i in range(K, N):
        if len(kinds) == K:
            break
        if TD[i][0] not in kinds:
            kinds.add(TD[i][0])
            total += TD[i][1]
            for j in range(i - 1, -1, -1):
                if TD[j][0] not in kinds:
                    kinds.add(TD[j][0])
                    total -= TD[j][1]
                    ans = max(ans, total + len(kinds) ** 2)
                    break
    print(ans)

=======
Suggestion 7

def main():
    N, K = [int(x) for x in input().split()]
    T = [0 for _ in range(N)]
    D = [0 for _ in range(N)]
    for i in range(N):
        t, d = [int(x) for x in input().split()]
        T[i] = t
        D[i] = d
    #print(N, K)
    #print(T)
    #print(D)

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by deliciousness in descending order.
    # 2. For each sorted deliciousness, find the maximum satisfaction.
    # 3. Then, find the maximum of the maximum satisfactions.
    # 4. The maximum satisfaction is the answer.

    # 1. Sort by

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        t, d = map(int, input().split())
        S.append((t, d))
    S.sort(key=lambda x: x[1], reverse=True)
    D = defaultdict(int)
    D[S[0][0]] = 1
    X = [S[0][1]]
    for i in range(1, K):
        D[S[i][0]] += 1
        X.append(S[i][1])
    x = len(D)
    ans = sum(X) + x*x
    for i in range(K, N):
        if D[S[i][0]] > 0:
            D[S[i][0]] += 1
            X.append(S[i][1])
            continue
        D[S[i][0]] += 1
        X.append(S[i][1])
        X.sort()
        x += 1
        ans = max(ans, sum(X[:-1]) + x*x)
    print(ans)

=======
Suggestion 9

def solve(N, K, t, d):
    # write your code here
    # return ans

=======
Suggestion 10

def read_int():
    return int(input())
