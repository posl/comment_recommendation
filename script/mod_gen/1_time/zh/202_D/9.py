def main():
    #读取输入
    A, B, K = map(int, input().split())
    #定义函数
    def combination(A, B):
        if A == 0 or B == 0:
            return 1
        else:
            return combination(A-1, B) + combination(A, B-1)
    #定义函数
    def make_string(A, B, K):
        if A == 0:
            return 'b' * B
        elif B == 0:
            return 'a' * A
        else:
            if K <= combination(A-1, B):
                return 'a' + make_string(A-1, B, K)
            else:
                return 'b' + make_string(A, B-1, K-combination(A-1, B))
    #输出结果
    print(make_string(A, B, K))

if __name__ == '__main__':
    main()