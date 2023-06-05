def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_num = max(a)
    for i in range(n):
        if a[i] == max_num:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_num)
