def main():
    A,B = map(int,input().split())
    if A+B <= 9999999999:
        print("Easy")
    else:
        print("Hard")
