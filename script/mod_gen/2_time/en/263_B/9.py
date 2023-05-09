def main():
    n = int(input())
    parents = list(map(int, input().split()))
    parents.insert(0,0)
    #print(parents)
    #print(parents[n])
    count = 0
    while parents[n] != 1:
        n = parents[n]
        count += 1
    print(count+1)

if __name__ == '__main__':
    main()