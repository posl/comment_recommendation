def num2str(n):
    if n <= 26:
        return chr(n + 96)
    else:
        return num2str((n - 1) // 26) + chr((n - 1) % 26 + 97)
n = int(input())
print(num2str(n))
