def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        max = 0
        for j in range(n):
            if i != j and a[j] > max:
                max = a[j]
        print(max)
