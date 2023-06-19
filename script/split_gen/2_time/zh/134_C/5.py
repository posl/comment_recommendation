def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max = 0
    for i in range(n):
        if max < a[i]:
            max = a[i]
    for i in range(n):
        if max == a[i]:
            a[i] = 0
    for i in range(n):
        print(max(a))
