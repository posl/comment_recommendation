def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for i in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    for i in range(Q):
        s = S
        t = T[i]
        k = K[i]
        for j in range(t):
            s = s.replace('A','BC')
            s = s.replace('B','CA')
            s = s.replace('C','AB')
        print(s[k-1])
