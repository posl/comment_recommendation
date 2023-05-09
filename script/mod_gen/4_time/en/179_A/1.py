def plural(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'
word = input()
print(plural(word))

if __name__ == '__main__':
    plural()