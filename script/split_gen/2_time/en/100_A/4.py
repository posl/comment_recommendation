def main():
    A,B = map(int,input().split())
    if A+B <= 16 and A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")
main()
