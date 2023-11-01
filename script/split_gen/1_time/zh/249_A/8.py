def main():
    A,B,C,D,E,F,X = map(int,input().split())
    takahashi = 0
    aoki = 0
    while True:
        if takahashi + aoki == X:
            break
        if takahashi < aoki:
            takahashi += A
            aoki -= D
        else
