def main():
    N = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if p[i] == i+1:
            count += 1
    if count == N:
        print("YES")
    elif count == N-2:
        print("YES")
    else:
        print("NO")
main()
