def problems146_b():
    n = int(input())
    s = input()
    result = ''
    for i in s:
        if ord(i) + n > ord('Z'):
            result += chr(ord(i) + n - ord('Z') + ord('A') - 1)
        else:
            result += chr(ord(i) + n)
    print(result)

if __name__ == '__main__':
    problems146_b()