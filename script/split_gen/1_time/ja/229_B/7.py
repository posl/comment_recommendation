def main():
    a,b = map(int,input().split())
    if a+b < 10**(len(str(a))):
        print("Easy")
    else:
        print("Hard")
