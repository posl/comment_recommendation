def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = [0]*10**5
    c2 = [0]*10**5
    for i in range(n//2):
        c1[v1[i]-1] += 1
        c2[v2[i]-1] += 1
    m1 = max(c1)
    m2 = max(c2)
    if c1.index(m1) == c2.index(m2):
        m1 = max(c1[0:c1.index(m1)]+[0]+c1[c1.index(m1)+1:])
        m2 = max(c2[0:c2.index(m2)]+[0]+c2[c2.index(m2)+1:])
    print(n - m1 - m2)
main()
