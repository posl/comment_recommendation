def get_dog_name(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        name = ''
        while n > 0:
            name = chr(ord('a') + (n - 1) % 26) + name
            n = (n - 1) // 26
        return name
n = int(input())
print(get_dog_name(n))

if __name__ == '__main__':
    get_dog_name()