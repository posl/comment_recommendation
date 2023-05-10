def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if all(s in T for s in S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()