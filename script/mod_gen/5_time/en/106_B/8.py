def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            divisors = 0
            for j in range(1,i+1):
                if i % j == 0:
                    divisors += 1
            if divisors == 8:
                count += 1
    print(count)
main()
