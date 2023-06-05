def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if i+1 != p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()