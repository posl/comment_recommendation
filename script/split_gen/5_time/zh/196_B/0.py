def main():
    import sys
    try:
        input = sys.stdin.readline
        x = float(input())
        print(int(x+0.5))
    except:
        print("输入有误")
