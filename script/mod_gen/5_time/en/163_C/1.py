def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in A:
        B[i-1] += 1
    for i in B:
        print(i)

if __name__ == '__main__':
    main()