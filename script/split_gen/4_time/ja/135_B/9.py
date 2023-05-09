def main():
    N = int(input())
    p = list(map(int, input().split()))
    answer = "YES"
    for i in range(N):
        if p[i] != i+1:
            answer = "NO"
    print(answer)
