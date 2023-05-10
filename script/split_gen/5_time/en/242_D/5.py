def main():
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        t, k = map(int, input().split())
        query.append([t, k])
    t_max = max([t for t, k in query])
    s = S
    for t in range(1, t_max+1):
        s = s.replace('A', 'BC')
        s = s.replace('B', 'CA')
        s = s.replace('C', 'AB')
    for t, k in query:
        print(s[k-1])
