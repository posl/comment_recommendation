def main():
    #读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    #解决方案1
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[-k])
    #解决方案2
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i], reverse=True)[k-1])
    #解决方案3
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[i-k])
    #解决方案4
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i], reverse=True)[k-1])
    #解决方案5
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[i-k])
    #解决方案6
    #问题陈述中的指定值
    for i in range(k, n+1):
        print(sorted(p[:i], reverse=True)[k-1])
