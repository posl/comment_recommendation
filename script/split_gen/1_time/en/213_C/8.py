def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i
    for i in range(len(b)):
        b_dict[b[i]] = i
    for i in range(n):
        print(a_dict[a[i]] + 1, b_dict[b[i]] + 1)
