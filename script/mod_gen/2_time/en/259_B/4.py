def main():
    a, b, d = map(int, input().split())
    theta = math.radians(d)
    a_prime = a * math.cos(theta) - b * math.sin(theta)
    b_prime = a * math.sin(theta) + b * math.cos(theta)
    print(a_prime, b_prime)

if __name__ == '__main__':
    main()