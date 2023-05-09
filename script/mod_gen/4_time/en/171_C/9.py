def answer(n):
    #print(n)
    if n <= 26:
        return chr(n + 96)
    else:
        m = n
        s = ''
        while m > 0:
            s = chr((m-1)%26 + 97) + s
            m = (m-1) // 26
        return s

if __name__ == '__main__':
    answer()