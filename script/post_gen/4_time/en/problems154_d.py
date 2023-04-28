Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(N):
        p[i] = (p[i] + 1) / 2
    s = sum(p[:K])
    ans = s
    for i in range(N - K):
        s += p[i + K] - p[i]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(N-K):
        tmp = tmp - (p[i]+1)/2 + (p[i+K]+1)/2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    e = [0] * N
    for i in range(N):
        e[i] = (p[i] + 1) / 2
    sum = 0
    for i in range(K):
        sum += e[i]
    max = sum
    for i in range(K, N):
        sum += e[i]
        sum -= e[i - K]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (p[i + k] - p[i]) / 2 + p[i])
    print(ans)

main()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    for i in range(k, n):
        s = max(s, s - p[i-k] + p[i])
    print((s + k) / 2)

=======
Suggestion 6

def dice(N, K, p):
    p = [0] + p
    for i in range(1, N+1):
        p[i] += p[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, p[i+K]-p[i])
    return (ans+K)/2

N, K = map(int, input().split())
p = list(map(int, input().split()))
print(dice(N, K, p))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #print(N, K, p)
    #print([sum(p[i:i+K]) for i in range(N-K+1)])
    print(max([sum(p[i:i+K]) for i in range(N-K+1)]) / 2 + K / 2)

=======
Suggestion 8

def dice():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    max_sum = 0
    for i in range(N-K+1):
        sum = 0
        for j in range(K):
            sum += p[i+j]
        if sum > max_sum:
            max_sum = sum
    return max_sum/2

print(dice())

=======
Suggestion 9

def get_expected_value(n, k, p):
    expected_value = 0
    for i in range(n - k + 1):
        expected_value += (k * (k + 1) / 2) / k * sum(p[i:i + k]) / k
    return expected_value

=======
Suggestion 10

def dice(n,k,p):
    #n - number of dice
    #k - number of dice to be chosen
    #p - list of sides of each die
    #return - max expected sum of k dice
    #print("n=",n,"k=",k,"p=",p)
    #print("p[0:k]=",p[0:k])
    #print("sum(p[0:k])=",sum(p[0:k]))
    max_expected_sum = sum(p[0:k])
    for i in range(1,n-k+1):
        #print("i=",i)
        #print("p[i:i+k]=",p[i:i+k])
        #print("sum(p[i:i+k])=",sum(p[i:i+k]))
        if sum(p[i:i+k]) > max_expected_sum:
            max_expected_sum = sum(p[i:i+k])
    return max_expected_sum
