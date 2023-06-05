def main():
    N = int(input())
    x = list(map(int,input().split()))
    #曼哈顿距离
    print(sum(map(abs,x)))
    #欧氏距离
    print(sum(map(lambda x:x**2,x))**0.5)
    #切比雪夫距离
    print(max(map(abs,x)))

if __name__ == '__main__':
    main()