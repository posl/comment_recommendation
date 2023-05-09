def main():
    n = input()
    n = list(n)
    for i in range(len(n)):
        if n[i] == '1':
            n[i] = '9'
        elif n[i] == '9':
            n[i] = '1'
    print(''.join(n))
main()
