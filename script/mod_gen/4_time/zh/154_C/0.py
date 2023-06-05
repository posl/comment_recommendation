def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if len(set(a)) == len(a) else "NO")

if __name__ == '__main__':
    main()