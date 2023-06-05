def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [i for i in range(2**n)]
    for i in range(n):
        c = []
        for j in range(2**(n-i-1)):
            if a[b[j*2]] > a[b[j*2+1]]:
                c.append(b[j*2])
            else:
                c.append(b[j*2+1])
        b = c
    if a[b[0]] < a[b[1]]:
        print(b[0]+1)
    else:
        print(b[1]+1)
