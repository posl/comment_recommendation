def main():
    # get input
    A, B, C, D, E = map(int, input().split())
    # sort input
    numbers = sorted([A, B, C, D, E])
    # check for full house
    if numbers[0] == numbers[1] == numbers[2] != numbers[3] != numbers[4]:
        if numbers[3] == numbers[4]:
            print('Yes')
            return
    if numbers[0] != numbers[1] != numbers[2] == numbers[3] == numbers[4]:
        if numbers[0] == numbers[1]:
            print('Yes')
            return
    print('No')
