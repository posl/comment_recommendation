def main():
    #输入
    A, B = map(int, input().split())
    #处理
    #A个插座的电源条可以将一个空插座扩展到A个空插座。
    #所以只要B>A，就可以用一个电源条扩展到B个空插座
    #所以，只要B>A，就需要的电源条数就是1个
    #如果B<=A，那么就需要的电源条数就是B//A+1
    if B<=A:
        ans = 1
    else:
        ans = B//A+1
    #输出
    print(ans)

if __name__ == '__main__':
    main()