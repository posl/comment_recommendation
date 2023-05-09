def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxAindex = A.index(maxA)
    A.pop(maxAindex)
    maxA2 = max(A)
    for i in range(N):
        if i == maxAindex:
            print(maxA2)
        else:
            print(maxA)
main()

if __name__ == '__main__':
    main()