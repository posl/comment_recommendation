def main():
    print("输入三个数字，用空格分隔：")
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and a !
