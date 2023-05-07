def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Count the number of cards
    num_cards = [0] * (N + 1)
    for a in A:
        num_cards[a] += 1
    for i in range(1, N + 1):
        if num_cards[i] % 2 == 1:
            print(i)
            return
main()
I think I have to use a dictionary to count the number of cards. But I'm not sure how to do it. Any help would be appreciated.
I am trying to make a program that takes a list of numbers and prints the numbers that are repeated in the list. I have been trying to use a dictionary to do this, but I can't seem to get it to work. Here is my code:

if __name__ == '__main__':
    main()