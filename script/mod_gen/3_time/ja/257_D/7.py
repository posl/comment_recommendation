def main():
    N = int(input())
    jumppoint = []
    for i in range(N):
        jumppoint.append(list(map(int, input().split())))
    print(jumppoint)

if __name__ == '__main__':
    main()