def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(sorted(a)[n-2])
        else:
            print(max_a)
