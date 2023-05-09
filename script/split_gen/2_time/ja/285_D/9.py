def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    # s と t が完全に一致している場合は、変更ができない
    if s == t:
        print("No")
        return
    # s と t が一致していない場合は、変更ができる
    print("Yes")
