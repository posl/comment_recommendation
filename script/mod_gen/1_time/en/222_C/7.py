def play(hands):
    #print(hands)
    n = len(hands)
    if n == 2:
        if hands[0] == 'G' and hands[1] == 'C':
            return 0
        elif hands[0] == 'C' and hands[1] == 'P':
            return 0
        elif hands[0] == 'P' and hands[1] == 'G':
            return 0
        elif hands[0] == hands[1]:
            return -1
        else:
            return 1
    else:
        mid = n // 2
        left = play(hands[:mid])
        right = play(hands[mid:])
        if left == right:
            return left
        elif left > right:
            return left
        else:
            return right + mid

if __name__ == '__main__':
    play()