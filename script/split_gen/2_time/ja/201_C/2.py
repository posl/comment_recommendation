def main():
    S = input()
    if S[0] == "o":
        if S[1] == "o":
            if S[2] == "o":
                if S[3] == "o":
                    if S[4] == "o":
                        if S[5] == "o":
                            if S[6] == "o":
                                if S[7] == "o":
                                    if S[8] == "o":
                                        if S[9] == "o":
                                            print(1)
                                        elif S[9] == "x":
                                            print(0)
                                        else:
                                            print(10)
                                    elif S[8] == "x":
                                        if S[9] == "o":
                                            print(0)
                                        elif S[9] == "x":
                                            print(0)
                                        else:
                                            print(9)
                                    else:
                                        if S[9] == "o":
                                            print(10)
                                        elif S[9] == "x":
                                            print(9)
                                        else:
                                            print(90)
                                elif S[7] == "x":
                                    if S[8] == "o":
                                        if S[9] == "o":
                                            print(0)
                                        elif S[9] == "x":
                                            print(0)
                                        else:
                                            print(9)
                                    elif S[8] == "x":
                                        if S[9] == "o":
                                            print(0)
                                        elif S[9] == "x":
                                            print(0)
                                        else:
                                            print(8)
                                    else:
                                        if S[9] == "o":
                                            print(9)
                                        elif S[9] == "x":
                                            print(8)
                                        else:
                                            print(81)
                                else:
                                    if S[7] == "o":
                                        if S[8] == "o":
                                            if S[9] == "o":
                                                print(10)
                                            elif S[9] == "x":
                                                print(9)
                                            else:
                                                print(90)
                                        elif S[8] == "x":
                                            if S[9] == "o":
                                                print(9)
                                            elif S[9] == "x":
                                                print(8)
                                            else:
                                                print(81)
                                        else:
                                            if S[9] == "o":
                                                print(90)
                                            elif
