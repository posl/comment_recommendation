def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    count = 0
    max = 0
    for i in range(N):
        if T[i] > max:
            count = i + 1
            max = T[i]
    print(count)
