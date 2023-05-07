def main():
    N = int(input())
    c = input()
    W = 0
    R = 0
    for i in range(N):
        if c[i] == 'W':
            W += 1
        else:
            R += 1
    print(min(W, R))
