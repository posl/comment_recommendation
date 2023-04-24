Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i%A != 0 and i%B != 0:
            ans += i
    print(ans)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(N * (N + 1) // 2 - (A * (N // A) * (N // A + 1) // 2 + B * (N // B) * (N // B + 1) // 2 - A * B * (N // (A * B)) * (N // (A * B) + 1) // 2))

=======
Suggestion 3

def main():
    N,A,B = map(int,input().split())
    print(N*(N+1)//2 - A*(N//A)*(N//A+1)//2 - B*(N//B)*(N//B+1)//2 + A*B*(N//(A*B))*(N//(A*B)+1)//2)

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print(N - (N // A + N // B - N // (A * B)))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print(N - (N//A + N//B - N//lcm(A,B)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    print((N // A + N // B) - N // lcm(A, B))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    sumA = (N // A) * (N // A + 1) // 2 * A
    sumB = (N // B) * (N // B + 1) // 2 * B
    sumAB = (N // (A * B)) * (N // (A * B) + 1) // 2 * (A * B)
    print(sumA + sumB - sumAB)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    # n = 10
    # a = 3
    # b = 5
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    # 1 以上 N 以下の整数

=======
Suggestion 9

def lcm(x,y):
    return (x * y) // math.gcd(x,y)
