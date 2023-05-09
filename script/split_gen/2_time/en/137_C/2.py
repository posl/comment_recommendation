def main():
    N = int(input())
    s = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(s[i]) == sorted(s[j]):
                count += 1
    print(count)
