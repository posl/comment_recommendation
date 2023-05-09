def S(n):
    if n < 10:
        return n
    else:
        return n%10 + S(n//10)

if __name__ == '__main__':
    S()