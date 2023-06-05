def main():
    dice = input().split()
    print(21 - int(dice[0]) - int(dice[1]) - int(dice[2]))

if __name__ == '__main__':
    main()