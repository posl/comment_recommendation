def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    import itertools
    l = list(itertools.permutations(range(n)))
    ans = 0
    for i in l:
        for j in range(n-1):
            ans += ((xy[i[j]][0]-xy[i[j+1]][0])**2+(xy[i[j]][1]-xy[i[j+1]][1])**2)**0.5
    print(ans/len(l))

if __name__ == '__main__':
    main()