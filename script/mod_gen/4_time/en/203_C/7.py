def main():
    n,k = map(int, input().split())
    ab = []
    for i in range(n):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort()
    #print(ab)
    i = 0
    while k > 0:
        if i >= n:
            break
        if ab[i][0] <= k:
            k += ab[i][1]
        i += 1
    print(k)

if __name__ == '__main__':
    main()