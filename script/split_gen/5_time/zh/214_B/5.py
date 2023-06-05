def main():
    #print("请输入两个整数，空格隔开：")
    #s,t = input().split()
    #s,t = 1,0
    #s,t = 2,5
    #s,t = 10,10
    s,t = 30,100
    s,t = int(s),int(t)
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
                    #print(a,b,c)
    print(count)
