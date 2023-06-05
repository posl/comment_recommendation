def solve(n,k,s):
    # 从左向右遍历
    # 从左向右遍历，如果是L，记录下来
    # 如果是R，如果前面有L，记录下来
    # 如果是R，如果前面没有L，记录下来
    # 如果是R，如果前面有R，不记录下来
    # 从右向左遍历
    # 从右向左遍历，如果是R，记录下来
    # 如果是L，如果前面有R，记录下来
    # 如果是L，如果前面没有R，记录下来
    # 如果是L，如果前面有L，不记录下来
    # 遍历两遍，得到两个数组，分别记录从左向右和从右向左的快乐人数
    # 如果k<=n/2，那么遍历两个数组，取出前k个最大的数，相加即可
    # 如果k>n/2，那么遍历两个数组，取出所有的数，相加即可
    # 如果k==n/2，那么遍历两个数组，取出所有的数，相加即可
    l = []
    r = []
    l.append(0)
    r.append(0)
    for i in range(n):
        if s[i] == 'L':
            l.append(i+1)
        else:
            if len(l) == 1:
                pass
            elif s[l[-1]-1] == 'L':
                l.append(i+1)
            else:
                pass
    for i in range(n-1,-1,-1):
        if s[i] == 'R':
            r.append(n-i)
        else:
            if len(r) == 1:
                pass
            elif s[n-r[-1]] == 'R':
                r.append(n-i)
            else:
                pass
    if k <= n/2:
        l.sort(reverse=True)
        r.sort(reverse=True)
        print(sum(l[:k]) + sum(r[:k]))
    else:
        print(sum(l) + sum(r))
