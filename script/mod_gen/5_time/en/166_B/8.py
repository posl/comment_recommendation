def main():
    n,k = map(int, input().split())
    a = [0]*n
    for i in range(k):
        d = int(input())
        a += list(map(int, input().split()))
    print(n-len(set(a)))

if __name__ == '__main__':
    main()