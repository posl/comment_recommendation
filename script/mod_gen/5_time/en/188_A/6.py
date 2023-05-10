def main():
    scores = input().split(' ')
    if int(scores[0]) > int(scores[1]):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()