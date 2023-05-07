def main():
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    d = int(inp[3])
    if a == c:
        if b < d:
            print('Takahashi')
        else:
            print('Aoki')
    elif a < c:
        print('Takahashi')
    else:
        print('Aoki')
