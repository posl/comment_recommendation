def main():
    X, Y, Z = map(int, input().split())
    if X > 0:
        if Y > 0:
            if Z > 0:
                if X > Y:
                    if X > Z:
                        if Y > Z:
                            print(X - Y + X - Z)
                        else:
                            print(X - Y + Z - Y)
                    else:
                        print(X - Y + Z - X)
                else:
                    if X > Z:
                        print(Y - X + X - Z)
                    else:
                        print(Y - X + Z - X)
            else:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
        else:
            if Z > 0:
                if X > Z:
                    print(X - Y + X - Z)
                else:
                    print(X - Y + Z - X)
            else:
                print(X - Y + X - Z)
    else:
        if Y > 0:
            if Z > 0:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
            else:
                print(X - Y + X - Z)
        else:
            if Z > 0:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
            else:
                print(X - Y + X - Z)
