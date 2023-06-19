def main():
    v,t,s,d = map(int,input("请输入V T S D:").split())
    if d < v*t or d > v*s:
        print("Yes")
    else:
        print("No")
