def main():
    a,b,q = map(int,input().split())
    s = [0] * (a+2)
    s[0] = -float('inf')
    s[-1] = float('inf')
    for i in range(1,a+1):
        s[i] = int(input())
    t = [0] * (b+2)
    t[0] = -float('inf')
    t[-1] = float('inf')
    for i in range(1,b+1):
        t[i] = int(input())
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    for i in range(q):
        for j in range(a+1):
            if s[j] <= x[i] < s[j+1]:
                a1 = x[i] - s[j]
                a2 = s[j+1] - x[i]
                break
        for j in range(b+1):
            if t[j] <= x[i] < t[j+1]:
                b1 = x[i] - t[j]
                b2 = t[j+1] - x[i]
                break
        print(min(max(a1,b1),max(a2,b2),a1*2+b2,b1*2+a2))
