def main():
    #读取输入
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #计算答案
    ans = 0
    if A % 10 != 0:
        ans += (A // 10 + 1) * 10
    else:
        ans += A
    if B % 10 != 0:
        ans += (B // 10 + 1) * 10
    else:
        ans += B
    if C % 10 != 0:
        ans += (C // 10 + 1) * 10
    else:
        ans += C
    if D % 10 != 0:
        ans += (D // 10 + 1) * 10
    else:
        ans += D
    if E % 10 != 0:
        ans += (E // 10 + 1) * 10
    else:
        ans += E
    #输出结果
    print(ans)

if __name__ == '__main__':
    main()