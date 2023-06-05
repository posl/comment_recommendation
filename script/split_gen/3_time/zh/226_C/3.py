def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_i, k_i, *a_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
        a.append(a_i)
    t_max = max(t)
    t_min = min(t)
    t_sum = sum(t)
    print(t_max + t_sum)
