def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != q[i]:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")
