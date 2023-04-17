Synthesizing 10/10 solutions

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]
    for a in A:
        B.append((B[-1] + a) % M)
    from collections import Counter
    C = Counter(B)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]
    for i in range(N):
        B.append((B[-1] + A[i]) % M)
    D = {}
    for b in B:
        D[b] = D.get(b, 0) + 1
    ans = 0
    for v in D.values():
        ans += v * (v - 1) // 2
    print(ans)

main()

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    mod = [0] * M
    mod[0] = 1
    sumA = 0
    for a in A:
        sumA += a
        sumA %= M
        ans += mod[sumA]
        mod[sumA] += 1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0]
    for i in range(N):
        sum_A.append((sum_A[i] + A[i]) % M)
    count = [0] * M
    for i in range(N + 1):
        count[sum_A[i]] += 1
    ans = 0
    for i in range(M):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

=======

def main():
    import sys
    from collections import defaultdict
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    D = defaultdict(int)
    for i in range(N + 1):
        D[S[i]] += 1
    ans = 0
    for k in D.keys():
        ans += D[k] * (D[k] - 1) // 2
    print(ans)

main()

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    A = [sum(A[:i+1]) % M for i in range(N+1)]

    ans = 0
    for i in range(N+1):
        ans += A[:i].count(A[i])

    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, M)
    # print(A)
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum % M == 0:
                ans += 1
    print(ans)

=======

def main():

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]

    # 余りごとの数
    c = [0] * M
    for i in range(N + 1):
        c[s[i] % M] += 1

    # 組み合わせ
    ans = 0
    for i in range(M):
        ans += c[i] * (c[i] - 1) // 2

    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    if sum % M == 0:
        print(N*(N+1)//2)
        return
    else:
        sum = 0
        A = [0] + A
        for i in range(1, N+1):
            A[i] += A[i-1]
        #print(A)
        A = [a % M for a in A]
        #print(A)
        d = dict()
        for a in A:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        #print(d)
        ans = 0
        for k, v in d.items():
            if v > 1:
                ans += v*(v-1)//2
        print(ans)
        return

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print('')

    sum = 0
    sum_list = []
    for a in A:
        sum += a
        sum_list.append(sum)

    #print(sum_list)
    #print('')

    mod_list = []
    for sum in sum_list:
        mod_list.append(sum % M)

    #print(mod_list)
    #print('')

    mod_dict = {}
    for mod in mod_list:
        if mod not in mod_dict:
            mod_dict[mod] = 1
        else:
            mod_dict[mod] += 1

    #print(mod_dict)
    #print('')

    count = 0
    for mod in mod_dict:
        count += mod_dict[mod] * (mod_dict[mod] - 1) // 2

    print(count)
