def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a_sorted[i]] = i + 1
        b_dict[b_sorted[i]] = i + 1
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])
