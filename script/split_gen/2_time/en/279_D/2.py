def main():
    A, B = map(int, input().split())
    if A <= B:
        print(A)
        return
    # A > B
    g = 1
    t = 0
    while True:
        t += B
        g += 1
        if A <= t + (A / (g ** 0.5)):
            print(t + (A / (g ** 0.5)))
            return
main()
import math
A,B=map(int,input().split())
