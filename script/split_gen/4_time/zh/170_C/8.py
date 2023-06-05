def main():
    X = int(input("请输入一个整数X："))
    N = int(input("请输入一个整数N："))
    p = [int(i) for i in input("请输入一个长度为N的整数序列：").split()]
    p.append(X)
    p.sort()
    for i in range(len(p)):
        if p[i] == X:
            if i == 0:
                print(p[i+1])
            elif i == len(p)-1:
                print(p[i-1])
            else:
                print(min(p[i-1],p[i+1]))
            break
