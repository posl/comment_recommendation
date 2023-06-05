def last_two_digits():
    while True:
        try:
            n = int(input())
            print(n%100)
        except:
            break

if __name__ == '__main__':
    last_two_digits()