def main():
    N = int(input())
    S = input()
    slimes = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            slimes += 1
    print(slimes)
