def main():
    a,b,c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        elif a < b:
            print("Aoki")
        else:
            print("Aoki")
    else:
        if a > b:
            print("Takahashi")
        elif a < b:
            print("Aoki")
        else:
            print("Takahashi")
