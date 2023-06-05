def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                count += 1
    if count <= 1:
        print("YES")
    else:
        print("NO")
