def mk_list(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        ret = []
        for i in range(1, m+1):
            for j in mk_list(n-1, m):
                if j[-1] < i:
                    ret.append(j + [i])
        return ret
n, m = map(int, input().split())
for i in mk_list(n, m):
    print(*i)

if __name__ == '__main__':
    mk_list()