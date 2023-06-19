def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        p, x = map(int, input().split())
        if p == 1:
            a[i] = x
        elif p == 2:
            for j in range(n):
                a[j] += x
        else:
            print(min(a))
            a.remove(min(a))
            a.append(0)

if __name__ == '__main__':
    main()