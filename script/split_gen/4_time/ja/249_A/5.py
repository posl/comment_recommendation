def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = 0
    H = 0
    while T <= X and H <= X:
        if T <= H:
            T += A
            H += D
        else:
            T += C
            H += E
    if T > H:
        print("Takahashi")
    elif T < H:
        print("Aoki")
    else:
        print("Draw")
