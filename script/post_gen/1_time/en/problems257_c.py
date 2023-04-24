Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < 50:
                count += 1
        else:
            if W[i] >= 50:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i - 1] != S[i]:
            ans += 1
    print(ans + 1)
    return

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, 10**9):
        cnt = 0
        for j in range(N):
            if S[j] == '0' and W[j] < i:
                cnt += 1
            elif S[j] == '1' and W[j] >= i:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W = sorted(W)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += N - i
        else:
            ans += i
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]

    w = []
    for i in range(N):
        if S[i] == '0':
            w.append(W[i])
    w.sort()
    w.append(10**10)

    ans = 0
    for i in range(N):
        if S[i] == '1':
            ind = bisect.bisect_left(w, W[i])
            if ind > ans:
                ans = ind
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    S = S[::-1]
    W = sorted(W)
    #print(S, W)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += N - i - W[i:].count(W[i])
        else:
            ans += W[:W.index(W[i])].count(W[i])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))

    W_sorted = sorted(W)
    W_sorted.append(-1)

    ans = 0
    for i in range(N):
        if S[i] == '0' and W_sorted[i] != W_sorted[i+1]:
            ans += 1
        elif S[i] == '1' and W_sorted[i] == W_sorted[i+1]:
            ans += 1

    print(ans)

main()

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.

I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?

I have tried to solve this problem using binary search. I

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # print(N)
    # print(S)
    # print(W)
    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    S = S.replace("0", "1")
    S = S.replace("1", "0")
    S = S.replace("0", "1")
    # print("S =", S)
    # print("S =", S)
    w = []
    for i in range(N):
        w.append((W[i], S[i]))
    # p

=======
Suggestion 9

def solve(N, S, W):
    # N = int(input())
    # S = input()
    # W = list(map(int, input().split()))
    # print(N, S, W)
    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # S = "10101"
    # W = [60, 45, 30, 40, 80]
    # N = len(S)

    # S = "000"
    # W = [1, 2, 3]
    # N = len(S)

    # S = "10101"
    # W = [60, 50, 50, 50, 60]
    # N = len(S)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    # print("")

    # print("S =", S)
    # print("W =", W)

    # print("N =", N)
    # print("S =", S)
    # print("
