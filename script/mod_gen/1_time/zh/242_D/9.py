def tr(s):
    return s.replace('a','bc').replace('b','ca').replace('c','ab')
S = input()
Q = int(input())
T = []
K = []
for i in range(Q):
    a,b = map(int,input().split())
    T.append(a)
    K.append(b)
for i in range(Q):
    s = S
    t = T[i]
    k = K[i]
    for j in range(t):
        s = tr(s)
    print(s[k-1])

if __name__ == '__main__':
    tr()