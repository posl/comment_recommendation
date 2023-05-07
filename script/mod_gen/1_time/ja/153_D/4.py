def f(H):
    if H == 1:
        return 1
    else:
        return 2*f(H//2)+1
H = int(input())
print(f(H))

if __name__ == '__main__':
    f()