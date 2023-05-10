def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        j = x - i
        if i*2 + j*4 == y:
            print('Yes')
            return
    print('No')
