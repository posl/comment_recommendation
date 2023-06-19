def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    score = 0
    for i in range(n):
        score += b[a[i] - 1]
        if i > 0 and a[i] - a[i - 1] == 1:
            score += c[a[i - 1] - 1]
    print(score)

if __name__ == '__main__':
    main()