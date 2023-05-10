def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        if i * i > N:
            break
        if N % i == 0:
            ans = i
    print(ans + N // ans - 2)
