def main():
    N = int(input())
    T = input()
    S = 0
    R = 0
    for i in range(N):
        if T[i] == "S":
            S += 1
        else:
            R += 1
    x = S - R
    y = N - 2 * R
    print(x, y)
