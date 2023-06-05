def f(n,m,lists):
    abs_lists = []
    for i in range(n):
        abs_lists.append([abs(lists[i][0]),abs(lists[i][1]),abs(lists[i][2])])
    abs_lists.sort(key=lambda x:x[0]+x[1]+x[2],reverse=True)
    print(abs_lists)
    ans = 0
    for i in range(m):
        ans += abs_lists[i][0]+abs_lists[i][1]+abs_lists[i][2]
    return ans

if __name__ == '__main__':
    f()