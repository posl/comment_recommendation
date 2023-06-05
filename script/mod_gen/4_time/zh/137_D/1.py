def main():
    n, m = map(int, input().split())
    ab_list = []
    for i in range(n):
        ab_list.append(list(map(int, input().split())))
    ab_list.sort(key = lambda x : x[0])
    #print(ab_list)
    ans = 0
    for i in range(n):
        if ab_list[i][0] > m:
            break
        else:
            ans += ab_list[i][1]
            m -= ab_list[i][0]
    print(ans)

if __name__ == '__main__':
    main()