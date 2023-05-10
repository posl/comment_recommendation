def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    if all(p[i] == i+1 for i in range(N)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()