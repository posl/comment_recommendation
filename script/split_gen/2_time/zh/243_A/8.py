def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]
    t_max = max(t_k, key=lambda x: x[0])[0]
    s = S
    for i in range(t_max):
        s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    for t, k in t_k:
        print(s[t:][k-1])
