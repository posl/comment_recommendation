def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = []
    for i in range(q):
        k.append(int(input()))
    for i in range(q):
        count = 0
        for j in range(1, 1000000000000000000):
            if j not in a:
                count += 1
                if count == k[i]:
                    print(j)
                    break

if __name__ == '__main__':
    main()