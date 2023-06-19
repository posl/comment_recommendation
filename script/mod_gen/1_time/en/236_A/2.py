def swap(S, a, b):
    return S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
S = input()
a, b = map(int, input().split())
print(swap(S, a, b))
