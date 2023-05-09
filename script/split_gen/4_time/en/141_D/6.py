def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    tickets = [0] * (m + 1)
    for i in range(n):
        tickets[0] += a[i]
        for j in range(m):
            if tickets[j] < tickets[j + 1]:
                tickets[j + 1] = tickets[j]
            tickets[j] //= 2
    print(tickets[m])
