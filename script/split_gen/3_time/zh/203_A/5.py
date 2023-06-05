def main():
    # 读入a,b,c
    a,b,c = map(int,input().split())
    # 逻辑处理
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)
