def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            if x == a:
                print(0)
            else:
                print(1)
        else:
            if x == a:
                print(0)
            else:
                if d > 0:
                    if a < x and x < a + d * n:
                        print(1)
                    else:
                        print(2)
                else:
                    if a + d * n < x and x < a:
                        print(1)
                    else:
                        print(2)
