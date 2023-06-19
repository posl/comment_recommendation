def main():
    x,y,a,b = map(int, input().split())
    exp = 0
    while x * a < x + b and x < y:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    print(exp)
main()
