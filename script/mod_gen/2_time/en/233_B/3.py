def reverse_string(L, R, S):
    return S[:L-1] + S[L-1:R][::-1] + S[R:]
L, R = map(int, input().split())
S = input()
print(reverse_string(L, R, S))

if __name__ == '__main__':
    reverse_string()