def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(n):
        mod[a[i] % 200] += 1
    for i in range(200):
        if mod[i] >= 2:
            print("Yes")
            count = 0
            for j in range(n):
                if a[j] % 200 == i:
                    count += 1
                    print(j + 1, end=" ")
                    if count == 2:
                        break
            print()
            count = 0
            for j in range(n):
                if a[j] % 200 == i:
                    count += 1
                    print(j + 1, end=" ")
                    if count == 2:
                        break
            print()
            return
    print("No")
