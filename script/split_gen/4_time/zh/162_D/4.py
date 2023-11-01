def main():
    N = int(input())
    S = input()
    r = 0
    g = 0
    b = 0
    for i in range(N):
        if S[i] == 'R':
            r += 1
        elif S[i] == 'G':
            g += 1
        else:
            b += 1
    ans = r * g * b
    for i in range(N):
