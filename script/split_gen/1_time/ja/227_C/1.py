def main():
    N = int(input())
    count = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            if a*b > N:
                break
            count += N//(a*b)
    print(count)
