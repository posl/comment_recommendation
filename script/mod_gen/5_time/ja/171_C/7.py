def num2alpha(num):
    if num <= 26:
        return chr(num + 96)
    else:
        return num2alpha((num - 1) // 26) + num2alpha(num % 26)
N = int(input())
print(num2alpha(N))

if __name__ == '__main__':
    num2alpha()