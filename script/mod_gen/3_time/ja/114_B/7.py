def main():
    S = input()
    num = 753
    diff = 1000
    for i in range(len(S)-2):
        if diff > abs(num - int(S[i:i+3])):
            diff = abs(num - int(S[i:i+3]))
    print(diff)

if __name__ == '__main__':
    main()