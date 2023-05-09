def prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return prime(x-2)
x = int(input())
while True:
    if prime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    prime()