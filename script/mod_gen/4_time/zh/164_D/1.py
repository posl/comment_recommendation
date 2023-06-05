def main():
    # 读取输入
    S = input()
    # 累积和
    A = [0] * (len(S) + 1)
    for i in range(len(S)):
        A[i + 1] = A[i] + int(S[i])
    # 计算每个余数的出现次数
    count = [0] * 2019
    for a in A:
        count[a % 2019] += 1
    # 计算答案
    ans = 0
    for c in count:
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()