def main():
    N = int(input())
    S = [1]
    for i in range(1,N):
        S = S + [i+1] + S
    print(*S)
