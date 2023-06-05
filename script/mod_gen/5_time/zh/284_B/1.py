def problem284_b():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input().split()
        count = 0
        for j in range(n):
            if int(a[j]) % 2 == 1:
                count += 1
        print(count)

if __name__ == '__main__':
    problem284_b()