def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print(len([a for a in A if a%2 == 1]))

if __name__ == '__main__':
    main()