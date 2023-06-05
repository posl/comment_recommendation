def judge(x):
    count = 0
    for i in range(N):
        if S[i] == '0' and W[i] < x:
            count += 1
    return count
N = int(input())
S = input()
W = list(map(int, input().split()))
left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if judge(mid) >= N // 2 + 1:
        right = mid
    else:
        left = mid
print(right)

if __name__ == '__main__':
    judge()