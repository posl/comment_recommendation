def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_k = input().split()
        t.append(int(t_k[0]))
        k.append(int(t_k[1]))
    for i in range(q):
        for j in range(t[i]):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k[i]-1])
