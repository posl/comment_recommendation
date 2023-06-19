def main():
    N = int(input())
    p = [0] * N
    for i in range(N):
        p[i] = int(input())
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

if __name__ == '__main__':
    main()