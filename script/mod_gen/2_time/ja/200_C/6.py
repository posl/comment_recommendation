def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i % 200 for i in A]
    cnt = 0
    for i in range(200):
        cnt += A.count(i) * (A.count(i) - 1) // 2
    print(cnt)

if __name__ == '__main__':
    main()