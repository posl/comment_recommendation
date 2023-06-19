def dog_name(N):
    N -= 1
    i = 1
    while N >= 26 ** i:
        N -= 26 ** i
        i += 1
    N += 1
    name = ''
    for j in range(i):
        name = chr(N % 26 + 97) + name
        N //= 26
    return name
N = int(input())
print(dog_name(N))
