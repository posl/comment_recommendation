def S(n):
    if n == 1:
        return "1"
    else:
        return S(n-1) + " " + str(n) + " " + S(n-1)
print(S(int(input())))

if __name__ == '__main__':
    S()