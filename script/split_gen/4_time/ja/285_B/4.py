def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while True:
            if i + l >= N:
                break
            if S[l] == S[i+l]:
                break
            l += 1
        print(l)
