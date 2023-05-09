def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if A[i] == (i+1):
            result += 1
    print(result//2)
main()
I solved this problem with the following code. I think this code is not elegant, but it works.

if __name__ == '__main__':
    main()