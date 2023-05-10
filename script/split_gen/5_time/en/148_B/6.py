def main():
    N = int(input())
    S,T = input().split()
    result = ""
    for i in range(N):
        result += S[i]
        result += T[i]
    print(result)
