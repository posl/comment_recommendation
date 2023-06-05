def main():
    N = int(input())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == 'L':
            L.append(i+1)
        else:
            R.append(i+1)
    L.reverse()
    print(' '.join(map(str, R+L)))
