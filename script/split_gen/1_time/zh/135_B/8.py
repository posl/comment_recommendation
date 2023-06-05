def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")
