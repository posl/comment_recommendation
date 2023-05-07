def main():
    n, m = map(int, input().split())
    # 1-indexed
    city = [list(map(int, input().split())) + [i] for i in range(m)]
    city.sort(key=lambda x: x[1])
    ans = [0] * m
    for i in range(m):
        ans[city[i][2]] = f'{city[i][0]:0>6}{i + 1:0>6}'
    print('
'.join(ans))

if __name__ == '__main__':
    main()