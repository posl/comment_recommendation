def main():
    a,b = map(int,input().split())
    if a+b >= 10**19:
        print("Hard")
    else:
        print("Easy")
