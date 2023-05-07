def takahashi(A, B, C, D):
    if (A <= 2 and B >= 2) or (C <= 2 and D >= 2):
        return "Aoki"
    else:
        return "Takahashi"
A, B, C, D = map(int, input().split())
print(takahashi(A, B, C, D))

if __name__ == '__main__':
    takahashi()