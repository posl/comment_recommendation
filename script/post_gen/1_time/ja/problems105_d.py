Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    s = [i % m for i in s]
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * M
    mod[0] = 1
    ans = 0
    mod_sum = 0
    for i in range(N):
        mod_sum += A[i]
        mod_sum %= M
        ans += mod[mod_sum]
        mod[mod_sum] += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
    A_mod = [0] * (N+1)
    for i in range(N+1):
        A_mod[i] = A_sum[i] % M
    A_mod_cnt = [0] * M
    for i in range(N+1):
        A_mod_cnt[A_mod[i]] += 1
    ans = 0
    for i in range(M):
        ans += A_mod_cnt[i] * (A_mod_cnt[i]-1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # バケット
    B = [0] * M
    for i in range(N + 1):
        B[S[i] % M] += 1
    # バケットの中の組み合わせ
    ans = 0
    for i in range(M):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * M
    mod[0] = 1
    total = 0
    for i in range(N):
        total = (total + A[i]) % M
        mod[total] += 1
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + [i % m for i in a]
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        a[i] %= m
    b = [0 for i in range(m)]
    for i in a:
        b[i] += 1
    ans = 0
    for i in b:
        ans += i * (i - 1) // 2
    print(ans)

main()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    # 累積和
    B = [0] * (N + 1)
    for i in range(N):
        B[i+1] = (B[i] + A[i]) % M

    # 累積和の値をキーにして、その値が出現するインデックスを保存する
    # 例えば、B = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4] のとき
    # C = {0: [0], 1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10], 4: [11, 12, 13]}
    C = {}
    for i, b in enumerate(B):
        if b in C:
            C[b].append(i)
        else:
            C[b] = [i]

    ans = 0
    for k, v in C.items():
        # 同じ値が出現するインデックスの差分を計算する
        # 例えば、B = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4] のとき
        # C = {0: [0], 1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10], 4: [11, 12, 13]}
        # のとき、v = [1, 2, 3] ならば、
        # 2 - 1 = 1
        # 3 - 2 = 1
        # 1 + 1 = 2
        # となり、2 が答えになる

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    #print(A)
    mod = [0] * M
    mod[0] = 1
    sum = 0
    for i in range(N):
        sum += A[i]
        sum %= M
        mod[sum] += 1
    #print(mod)
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a_i % m for a_i in a]
    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)
    d = {i: 0 for i in range(m)}
    for i in range(n+1):
        d[s[i]] += 1
    ans = 0
    for key, val in d.items():
        ans += val * (val - 1) // 2
    print(ans)

=======
Suggestion 10

def main
  n, m = gets.split.map(&:to_i)
  a = gets.split.map(&:to_i)
  count = 0
  sum = 0
  mod_a = Array.new(m, 0)
  mod_a[0] = 1
  a.each do |ai|
    sum += ai
    mod_a[sum % m] += 1
  end
  mod_a.each do |mod|
    count += mod * (mod - 1) / 2
  end
  puts count
end

main
