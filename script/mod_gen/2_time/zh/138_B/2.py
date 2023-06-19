def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    result = 0
    for i in range(N):
        result += 1/A[i]
    print(1/result)

if __name__ == '__main__':
    main()