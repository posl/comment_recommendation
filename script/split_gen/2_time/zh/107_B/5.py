def problems107_b(H, W, a):
    #print(H, W, a)
    ans = []
    for i in range(H):
        if not '#' in a[i]:
            continue
        ans.append(a[i])
    ans = list(zip(*ans))
    for i in range(len(ans)):
        if not '#' in ans[i]:
            continue
        ans[i] = ''.join(ans[i])
    ans = list(zip(*ans))
    for i in range(len(ans)):
        print(''.join(ans[i]))
