def main():
    a,b,c = map(int,input().split())
    if a > b:
        print("Takahashi")
    elif a < b:
        print("Aoki")
    elif a == b:
        if c == 0:
            print("Aoki")
        elif c == 1:
            print("Takahashi")
