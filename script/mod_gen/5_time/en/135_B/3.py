def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()