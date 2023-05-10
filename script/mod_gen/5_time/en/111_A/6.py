def replace_1_9(n):
    n = str(n)
    result = ''
    for i in range(0, len(n)):
        if n[i] == '1':
            result = result + '9'
        elif n[i] == '9':
            result = result + '1'
    return result
n = input()
print(replace_1_9(n))

if __name__ == '__main__':
    replace_1_9()