def run():
    A,B,C,D,E,F,X = map(int, input().split())
    takahashi = 0
    aoki = 0
    for i in range(1,X+1):
        if i % (A+B) <= A:
            takahashi += 1
        if i % (D+E) <= D:
            aoki += 1
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    run()