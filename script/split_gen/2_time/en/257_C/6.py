def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]
    W = W[::-1]
    S = S[::-1]
    #print(N, S, W)
    left = 0
    right = 10**9
    while right - left > 1:
        #print(left, right)
        mid = (left + right) // 2
        if check(mid, N, S, W):
            left = mid
        else:
            right = mid
    if check(right, N, S, W):
        print(right)
    else:
        print(left)
