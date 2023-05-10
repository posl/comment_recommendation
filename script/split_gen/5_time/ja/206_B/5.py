def main():
    N = int(input())
    sum = 0
    for i in range(1, 10**9+1):
        sum += i
        if sum >= N:
            print(i)
            break
