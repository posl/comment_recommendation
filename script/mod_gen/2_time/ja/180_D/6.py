def main():
    x, y, a, b = map(int, input().split())
    
    count = 0
    while True:
        if x * a >= x + b and x * a < y:
            x *= a
            count += 1
        elif x + b < y:
            x += b
            count += 1
        else:
            break
    
    print(count)
main()
