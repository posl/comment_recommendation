def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(k[i] + i)
        for j in range(n):
            if a[j] > k[i] + i:
                a.insert(j, k[i] + i)
                break
        else:
            a.append(k[i] + i)
    return

if __name__ == '__main__':
    main()