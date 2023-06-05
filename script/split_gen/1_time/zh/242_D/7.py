def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    for i in range(q):
        t_i = t[i]
        k_i = k[i]
        for j in range(t_i):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k_i-1])
