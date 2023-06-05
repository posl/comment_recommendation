def main():
    k = int(input())
    a, b = map(int, input().split())
    if (b//k)-(a-1)//k >= 1:
        print("OK")
    else:
        print("NG")
