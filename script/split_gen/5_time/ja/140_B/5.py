def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i != 0 and a[i] == a[i-1]+1:
            satisfaction += c[a[i-1]-1]
    print(satisfaction)
