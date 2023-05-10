def problem():
    S = input()
    a, b = map(int, input().split())
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    return S
print(problem())

if __name__ == '__main__':
    problem()