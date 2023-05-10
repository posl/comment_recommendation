def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        for j in range(t):
            s = s.replace('A', 'BC')
            s = s.replace('B', 'CA')
            s = s.replace('C', 'AB')
        print(s[k-1])
