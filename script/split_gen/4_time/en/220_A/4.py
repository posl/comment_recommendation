def main():
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            return
    print(-1)
