def main():
    n, k = map(int, input().split())
    prob = 0
    for i in range(1, n+1):
        if i >= k:
            prob += 1/n
        else:
            prob += (1/n)*(0.5**len(bin(k-i))-2)
    print(prob)
