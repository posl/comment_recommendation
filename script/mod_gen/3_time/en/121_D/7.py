def f(A, B):
    if (B - A + 1) % 2 == 0:
        return A ^ B
    else:
        return A ^ B ^ (A - 1)

if __name__ == '__main__':
    f()