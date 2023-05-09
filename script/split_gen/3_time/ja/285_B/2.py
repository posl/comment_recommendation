def main():
    N = int(input())
    S = input()
    for i in range(N-1):
        l = 0
        for j in range(N-i-1):
            if S[j] != S[j+i+1]:
                l += 1
            else:
                break
        print(l)
