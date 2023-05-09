def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    total = 0
    for i in range(N):
        if i == 0:
            total += p[i] / 2
        else:
            total += p[i]
    print(int(total))

if __name__ == '__main__':
    main()