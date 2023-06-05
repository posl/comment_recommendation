def problem262_c():
    n = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if min(data[i], data[j]) == i+1 and max(data[i], data[j]) == j+1:
                count += 1
    print(count)

if __name__ == '__main__':
    problem262_c()