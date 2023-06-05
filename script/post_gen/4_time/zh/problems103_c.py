Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_max(a_list):
    max_num = 0
    for i in range(1, max(a_list)+1):
        tmp = 0
        for j in a_list:
            tmp += i % j
        if tmp > max_num:
            max_num = tmp
    return max_num

=======
Suggestion 2

def f(m, a):
    sum = 0
    for i in range(len(a)):
        sum += m % a[i]
    return sum

=======
Suggestion 3

def f(m, a):
    ans = 0
    for i in range(len(a)):
        ans += m % a[i]
    return ans

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    f = [0] * (10 ** 5 + 1)
    for i in range(N):
        for j in range(1, 10 ** 5 // a[i] + 1):
            f[a[i] * j] += 1
    ans = 0
    for i in range(10 ** 5 + 1):
        ans += f[i] * i
    print(ans)

=======
Suggestion 5

def f(m, a):
    result = 0
    for i in a:
        result += m % i
    return result

=======
Suggestion 6

def f(m, a):
    sum = 0
    for i in range(len(a)):
        sum += m % a[i]
    return sum

n = int(input())
a = list(map(int, input().split()))

max = 0
max_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i

a.pop(max_index)

m = max
while True:
    if f(m, a) < f(m - 1, a):
        m -= 1
    else:
        break

print(f(m, a))

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()

    # 1. m mod a_1 + m mod a_2 + ... + m mod a_N = m mod (a_1 * a_2 * ... * a_N)
    # 2. 1 <= m mod (a_1 * a_2 * ... * a_N) < a_1 * a_2 * ... * a_N
    # 3. m mod (a_1 * a_2 * ... * a_N) = a_1 * a_2 * ... * a_N - 1
    # 4. m = k * (a_1 * a_2 * ... * a_N) + (a_1 * a_2 * ... * a_N - 1)
    # 5. f(m) = f(a_1 * a_2 * ... * a_N - 1) = a_1 * a_2 * ... * a_N * N - N
    # 6. f(m) = a_1 * a_2 * ... * a_N * N - N
    # 7. f(m) = a_1 * a_2 * ... * a_N * (N - 1)
    # 8. f(m) = a_1 * a_2 * ... * a_N * (N - 1) < a_1 * a_2 * ... * a_N * N
    # 9. f(m) < a_1 * a_2 * ... * a_N * N
    # 10. f(m) < a_1 * a_2 * ... * a_N * N = a_1 * a_2 * ... * a_N * (N - 1) = f(m)
    # 11. f(m) < f(m)
    # 12. f(m) = f(m)

    print(a[0] * a[1] * ... * a[N-1] * (N - 1))

=======
Suggestion 8

def max_f(a_list):
    #a_list.sort()
    a_list.reverse()
    #print(a_list)
    max_f = 0
    for i in range(1, a_list[0]+1):
        f = 0
        for a in a_list:
            f += i % a
        if f > max_f:
            max_f = f
    return max_f
