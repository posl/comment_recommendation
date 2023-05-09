def shift(string, n):
    return string[n:] + string[:n]
string = input()
strings = [shift(string, i) for i in range(len(string))]
print(min(strings))
print(max(strings))

if __name__ == '__main__':
    shift()