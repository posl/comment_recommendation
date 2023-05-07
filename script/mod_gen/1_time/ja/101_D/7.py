def main():
    K = int(input())
    suke = [1]
    for i in range(2, 10**15):
        if i % 10 == 0:
            continue
        if i % sum(int(n) for n in str(i)) == 0:
            suke.append(i)
        if len(suke) == K:
            break
    for i in range(K):
        print(suke[i])

if __name__ == '__main__':
    main()