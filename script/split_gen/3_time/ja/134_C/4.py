def main():
    n = int(input())
    a = list()
    for i in range(n):
        a.append(int(input()))
    max = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]
    for i in range(n):
        if a[i] == max:
            if i == 0:
                max2 = a[1]
            else:
                max2 = a[0]
            for j in range(n):
                if j != i:
                    if a[j] > max2:
                        max2 = a[j]
            print(max2)
        else:
            print(max)
