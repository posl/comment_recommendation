def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    satisfaction = 0
    prev = a[0]
    satisfaction += b[prev-1]
    for i in range(1, n):
        current = a[i]
        satisfaction += b[current-1]
        if prev + 1 == current:
            satisfaction += c[prev-1]
        prev = current
    print(satisfaction)
