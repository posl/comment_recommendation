def main():
    a,b,c = map(int, input().split())
    if c == 1:
        if a == b:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if a == b:
            print("Takahashi")
        else:
            print("Aoki")
