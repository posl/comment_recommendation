def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
    else:
        if x[0] == '9' and x[1] == '0':
            if x[2] == '1' and x[3] == '2':
                print("Weak")
            else:
                print("Strong")
        else:
            if x[0] == '8' and x[1] == '9':
                if x[2] == '0' and x[3] == '1':
                    print("Weak")
                else:
                    print("Strong")
            else:
                if x[0] == '7' and x[1] == '8':
                    if x[2] == '9' and x[3] == '0':
                        print("Weak")
                    else:
                        print("Strong")
                else:
                    if x[0] == '6' and x[1] == '7':
                        if x[2] == '8' and x[3] == '9':
                            print("Weak")
                        else:
                            print("Strong")
                    else:
                        if x[0] == '5' and x[1] == '6':
                            if x[2] == '7' and x[3] == '8':
                                print("Weak")
                            else:
                                print("Strong")
                        else:
                            if x[0] == '4' and x[1] == '5':
                                if x[2] == '6' and x[3] == '7':
                                    print("Weak")
                                else:
                                    print("Strong")
                            else:
                                if x[0] == '3' and x[1] == '4':
                                    if x[2] == '5' and x[3] == '6':
                                        print("Weak")
                                    else:
                                        print("Strong")
                                else:
                                    if x[0] == '2' and x[1] == '3':
                                        if x[2] == '4' and x[3] == '5':
                                            print("Weak")
                                        else:
                                            print("Strong")
                                    else:
                                        if x[0] == '1' and x[1] == '2':
                                            if x

if __name__ == '__main__':
    main()