def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_count = a.count(a_max)
    if a_max_count == 1:
        for i in range(n):
            if a[i] == a_max:
                print(max(a[:i] + a[i+1:]))
            else:
                print(a_max)
    else:
        for i in range(n):
            print(a_max)
