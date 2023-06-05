def main():
    # 读取输入
    N, K = map(int, input().split())
    S = input()
    # 将字符串S中的第K个字符下划线后打印出来
    print(S[:K - 1] + "_" + S[K - 1:])

if __name__ == '__main__':
    main()