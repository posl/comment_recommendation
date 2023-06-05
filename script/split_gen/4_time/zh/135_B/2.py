def main():
    # N = int(input())
    # p = list(map(int,input().split()))
    N = 5
    p = [2, 4, 3, 5, 1]
    # N = 7
    # p = [1, 2, 3, 4, 5, 6, 7]
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")
