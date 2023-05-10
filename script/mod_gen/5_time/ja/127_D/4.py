def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
                if i == n:
                    break
            else:
                break
        else:
            continue
        break
    print(sum(a))

if __name__ == '__main__':
    main()