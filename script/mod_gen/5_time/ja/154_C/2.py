def main():
    N = int(input())
    A = list(map(int, input().split()))
    print("YES" if len(A) == len(set(A)) else "NO")

if __name__ == '__main__':
    main()