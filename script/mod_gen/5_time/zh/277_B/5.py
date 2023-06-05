def main():
    n = int(input())
    card_list = []
    for i in range(n):
        card = input()
        card_list.append(card)
    if n == len(set(card_list)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()