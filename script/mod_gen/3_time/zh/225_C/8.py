def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**100):
        if B[0] == [i*7+j for j in range(1, 8)]:
            for j in range(1, N):
                if B[j] != [(i+j)*7+k for k in range(1, 8)]:
                    break
            else:
                print("Yes")
                break
    else:
        print("No")

if __name__ == '__main__':
    main()