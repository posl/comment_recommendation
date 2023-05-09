def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    print(sum(p) - max(p) // 2)

if __name__ == '__main__':
    main()