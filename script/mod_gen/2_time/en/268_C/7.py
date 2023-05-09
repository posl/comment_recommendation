def main():
    n = int(input())
    p = map(int, input().split())
    p = [i-1 for i in p]
    result = 0
    for i in range(n):
        if p[i] == i:
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
            result += 1
    print(result)

if __name__ == '__main__':
    main()