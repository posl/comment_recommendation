def main():
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print("".join(S))
