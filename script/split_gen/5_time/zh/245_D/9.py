def main():
    n,m = map(int, input().split())
    an = list(map(int, input().split()))
    cn = list(map(int, input().split()))
    bn = [0] * (m+1)
    for i in range(n+1):
        for j in range(m+1):
            bn[j] += an[i] * cn[i+j]
    print(' '.join(map(str, bn)))
