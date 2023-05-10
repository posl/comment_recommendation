def main():
    h, w, k = map(int, input().split())
    c_list = []
    for i in range(h):
        c_list.append(input())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k1 in range(h):
                for l1 in range(w):
                    if (i >> k1) & 1 == 0 and (j >> l1) & 1 == 0 and c_list[k1][l1] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()