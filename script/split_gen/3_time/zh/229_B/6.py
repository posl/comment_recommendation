def main():
    A,B = map(int,input().split())
    if A+B >= 10**9:
        print("Hard")
    else:
        print("Easy")
