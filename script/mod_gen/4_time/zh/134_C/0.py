def problems134_c():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_2nd = sorted(a)[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_max_2nd)
        else:
            print(a_max)

if __name__ == '__main__':
    problems134_c()