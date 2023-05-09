def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for a in A:
            if a % 2 == 1:
                odd += 1
        print(odd)

if __name__ == '__main__':
    main()