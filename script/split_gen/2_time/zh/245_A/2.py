def main():
    a,b,c,d = map(int, input().split())
    if a>b:
        print("Takahashi")
    elif a<b:
        print("Aoki")
    else:
        if c>d:
