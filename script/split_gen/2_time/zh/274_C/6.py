def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    for i in range(1, 2*n+1):
        j = i
        while True:
            print(b[j])
            if j == 1:
                break
            j = j//2
