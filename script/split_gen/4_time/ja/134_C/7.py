def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        a_sort = sorted(a)
        if a[i] == a_sort[-1]:
            print(a_sort[-2])
        else:
            print(a_sort[-1])
