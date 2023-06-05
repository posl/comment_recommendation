def main():
    S = input()
    i = 1
    for s in S:
        if i % 2 == 1:
            if s.islower() == False:
                print("No")
                exit()
        else:
            if s.isupper() == False:
                print("No")
                exit()
        i += 1
    print("Yes")
main()
