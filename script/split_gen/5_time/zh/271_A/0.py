def hexa(N):
    N = int(N)
    if N < 16:
        return '0' + hex(N)[2:].upper()
    else:
        return hex(N)[2:].upper()
N = input()
print(hexa(N))
