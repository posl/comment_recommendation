def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a-1] += 1
    for b in B:
        print(b)

if __name__ == '__main__':
    main()