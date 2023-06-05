def main():
    s = input()
    q = int(input())
    t_list = []
    k_list = []
    for i in range(q):
        t,k = map(int,input().split())
        t_list.append(t)
        k_list.append(k)
    for i in range(q):
        t = t_list[i]
        k = k_list[i]
        for j in range(t):
            s = s.replace('a','bc')
            s = s.replace('b','ca')
            s = s.replace('c','ab')
        print(s[k-1])
