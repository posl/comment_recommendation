def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i + 1 != p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")
