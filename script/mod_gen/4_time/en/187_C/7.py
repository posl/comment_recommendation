def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    words.sort()
    for i in range(N-1):
        if words[i] == "!" + words[i+1]:
            print(words[i+1])
            return
    print("satisfiable")
main()

if __name__ == '__main__':
    main()