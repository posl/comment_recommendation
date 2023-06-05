def main():
    #读取输入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #计算并输出答案
    print(sum(A))
    for i in range(Q):
        b, c = BC[i]
        print(sum(A) - A.count(b) * (b - c))

if __name__ == '__main__':
    main()