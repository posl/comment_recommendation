def dogName(N):
    dogName = ""
    while N > 0:
        N -= 1
        dogName = chr(ord('a') + N % 26) + dogName
        N /= 26
    return dogName

if __name__ == '__main__':
    dogName()