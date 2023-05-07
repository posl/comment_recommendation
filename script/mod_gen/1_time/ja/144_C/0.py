def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if N == 4:
        print(2)
        return
    if N == 5:
        print(3)
        return
    #i+jの最大値を探す
    i = 1
    j = 1
    while True:
        if i * j > N:
            break
        i += 1
        j += 1
    i -= 1
    j -= 1
    #Nがi*jの中央にあるかどうか
    if N == i * j:
        print(i + j - 2)
        return
    if N == i * j + i:
        print(i + j - 1)
        return
    if N == i * j + j:
        print(i + j - 1)
        return
    if N == i * j + i + j:
        print(i + j)
        return
    #Nがi*jの中央にない場合
    if N < i * j + i:
        print(i + j - 1)
        return
    if N < i * j + j:
        print(i + j - 1)
        return
    if N < i * j + i + j:
        print(i + j)
        return

if __name__ == '__main__':
    main()