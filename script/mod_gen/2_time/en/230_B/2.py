def main():
    S = input()
    T = 'o'*10**5 + 'x'*10**5 + 'o'*10**5
    for i in range(len(T)-len(S)+1):
        if T[i:i+len(S)] == S:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()