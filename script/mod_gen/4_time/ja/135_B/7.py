def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i, p in enumerate(P):
        if i+1 != p:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()