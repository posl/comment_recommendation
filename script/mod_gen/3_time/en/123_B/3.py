def main():
    # Get input here
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # Calculate result here
    result = 0
    if a%10 != 0:
        a += 10 - a%10
    if b%10 != 0:
        b += 10 - b%10
    if c%10 != 0:
        c += 10 - c%10
    if d%10 != 0:
        d += 10 - d%10
    if e%10 != 0:
        e += 10 - e%10
    result = a + b + c + d + e
    # Print result here
    print(result)
main()
