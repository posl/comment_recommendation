def main():
    #输入
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    #处理
    def permutation_to_number(p):
        n = len(p)
        r = 0
        for i in range(n):
            c = 0
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    c += 1
            r += c * math.factorial(n - i - 1)
        return r
    #输出
    print(abs(permutation_to_number(p) - permutation_to_number(q)))

if __name__ == '__main__':
    main()