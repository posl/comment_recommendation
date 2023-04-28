Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            if a * b > n:
                break
            for c in range(b, n + 1):
                if a * b * c > n:
                    break
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for A in range(1, N+1):
        for B in range(A, N+1):
            for C in range(B, N+1):
                if A*B*C <= N:
                    if A == B and B == C:
                        ans += 1
                    elif A == B or B == C:
                        ans += 3
                    else:
                        ans += 6
                else:
                    break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            if a * b > n:
                break
            for c in range(b, n+1):
                if a * b * c > n:
                    break
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i * j > n:
                break
            for k in range(j, n+1):
                if i * j * k > n:
                    break
                if i == j == k:
                    ans += 1
                elif i == j or j == k:
                    ans += 3
                else:
                    ans += 6
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i*j <= n:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i*j > N:
                break
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = n // (a*b)
            if c < b:
                break
            if n % (a*b) == 0:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            m = n // i
            for j in range(i, int(m ** 0.5) + 1):
                if m % j == 0:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        tmp = n // a
        for b in range(a, tmp+1):
            tmp2 = tmp // b
            if tmp2 >= b:
                ans += tmp2 - b + 1
    print(ans)

=======
Suggestion 10

def main():
    # 標準入力受け取り
    N = int(input())
    # Nの桁数を取得
    N_len = len(str(N))
    # Nの桁数が1桁の場合は、1桁の場合は、1からNまでの数を足す
    if N_len == 1:
        print(sum(range(1, N + 1)))
        exit()
    # Nの桁数が2桁以上の場合
    else:
        # Nの桁数-1の数を9の数で埋める
        N_9 = int('9' * (N_len - 1))
        # Nの桁数-1の数を9の数で埋めた数を足す
        sum_1 = sum(range(1, N_9 + 1))
        # Nの桁数-1の数を9の数で埋めた数を足した数を出力
        print(sum_1)
        # Nの桁数-1の数を9の数で埋めた数を足した数をNから引いた数を出力
        print(N - N_9)
        # Nの桁数-1の数を9の数で埋めた数を足した数をNから引いた数を9の数で埋めた数を足す
        sum_2 = sum(range(1, N - N_9 + 1))
        # Nの桁数-1の数を9の数で埋めた数を足した数をNから引いた数を9の数で埋めた数を足した数を出力
        print(sum_2)
        # Nの桁数-1の数を9の数で埋めた数を足した数をNから引いた数を9の数で埋めた数を足した数をNから引いた数を出力
        print(N - N_9 - sum_2)
        # Nの桁数-1の数を9の数で埋めた数を
