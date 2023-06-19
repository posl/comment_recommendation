def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = (A+B)*B
    aoki = (D+E)*E
    if taka > aoki:
        print("Takahashi")
    elif aoki > taka:
        print("Aoki")
    else:
        print("Draw")
main()
