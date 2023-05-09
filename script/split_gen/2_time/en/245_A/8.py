def problems245_a():
    A,B,C,D = map(int,input().split())
    Takahashi = A*60 + B
    Aoki = C*60 + D + 1
    if Takahashi < Aoki:
        print("Takahashi")
    else:
        print("Aoki")
