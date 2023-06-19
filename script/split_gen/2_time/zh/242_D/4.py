def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    for i in range(q):
        t = t_k[i][0]
        k = t_k[i][1]
        if t == 0:
            print(s[k - 1])
        else:
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
            print(s[k - 1])
