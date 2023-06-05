def main():
    # 读入数据
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    # 计算
    ans = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                continue
            break
        else:
            ans += 1
    # 打印结果
    print(ans)

if __name__ == '__main__':
    main()