def main():
    # Get the input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # Calculate the time
    if a % 10 != 0:
        a += 10 - (a % 10)
    if b % 10 != 0:
        b += 10 - (b % 10)
    if c % 10 != 0:
        c += 10 - (c % 10)
    if d % 10 != 0:
        d += 10 - (d % 10)
    if e % 10 != 0:
        e += 10 - (e % 10)
    # Calculate the time
    time = a + b + c + d + e
    # Print the time
    print(time)
main()

if __name__ == '__main__':
    main()