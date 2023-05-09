def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        s = S
        while t > 0:
            s = s.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
            t -= 1
        print(s[k-1])
