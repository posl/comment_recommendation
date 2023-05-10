def main():
    S = input()
    Q = int(input())
    s = S
    t = 0
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t_i -= t
        t = t_i
        k_i -= 1
        s = s[k_i:] + s[:k_i]
        s = s.replace("A", "BC")
        s = s.replace("B", "CA")
        s = s.replace("C", "AB")
        print(s[0])
