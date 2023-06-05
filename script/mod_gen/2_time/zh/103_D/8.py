def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab,key=lambda x:x[1])
    #print(ab)
    count = 0
    for i in range(m):
        if ab[i][0] == 1:
            count +=1
    print(count)

if __name__ == '__main__':
    main()