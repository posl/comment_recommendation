def main():
    N = int(input())
    S = input()
    result = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            result += 1
    print(result)
