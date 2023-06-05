def main():
    N = int(input())
    result = 0
    i = 2
    while i*i <= N:
        if N%i == 0:
            result += 1
            while N%i == 0:
                N //= i
        i += 1
    if N != 1:
        result += 1
    print(result)
    
main()
