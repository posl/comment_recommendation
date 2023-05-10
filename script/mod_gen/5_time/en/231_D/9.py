def main():
    n,m = map(int,input().split())
    a_b = []
    for i in range(m):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[1])
    #print(a_b)
    right = a_b[0][1]
    count = 1
    for i in range(1,m):
        if right <= a_b[i][0]:
            right = a_b[i][1]
            count += 1
    if count == m:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()