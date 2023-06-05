def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    print(sum([1 for i in d if i<=x]))

if __name__ == '__main__':
    main()