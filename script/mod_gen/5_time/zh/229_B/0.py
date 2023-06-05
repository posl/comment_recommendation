def main():
    a,b = map(int,input().split())
    if len(str(a+b)) > len(str(a)) or len(str(a+b)) > len(str(b)):
        print("Hard")
    else:
        print("Easy")
main()
