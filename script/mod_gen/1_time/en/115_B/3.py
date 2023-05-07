def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    result = 0
    for i in range(N):
        if i == 0:
            result += p[i] / 2
        else:
            result += p[i]
    print(int(result))

if __name__ == '__main__':
    main()