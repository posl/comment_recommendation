def get_alphabet():
    p = input().split()
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    for i in range(26):
        alphabet[int(p[i])-1] = chr(i+ord('a'))
    print(''.join(alphabet))
get_alphabet()
