def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] // 2
        else:
            sum += p[i]
    print(sum)

if __name__ == '__main__':
    main()