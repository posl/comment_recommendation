def last_two_digits():
    while True:
        try:
            n = int(input())
            print(n%100)
        except:
            break
