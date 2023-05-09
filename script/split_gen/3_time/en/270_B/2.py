def main():
    x, y, z = map(int, input().split())
    if x > 0:
        if y > 0:
            if z > 0:
                # x > 0, y > 0, z > 0
                if x > z:
                    print(x - y)
                else:
                    print(z - y + x)
            else:
                # x > 0, y > 0, z < 0
                if x > -z:
                    print(x - y)
                else:
                    print(-z - y + x)
        else:
            if z > 0:
                # x > 0, y < 0, z > 0
                if x > z:
                    print(x + y)
                else:
                    print(z + y + x)
            else:
                # x > 0, y < 0, z < 0
                if x > -z:
                    print(x + y)
                else:
                    print(-z + y + x)
    else:
        if y > 0:
            if z > 0:
                # x < 0, y > 0, z > 0
                if -x > z:
                    print(-x - y)
                else:
                    print(z - y - x)
            else:
                # x < 0, y > 0, z < 0
                if -x > -z:
                    print(-x - y)
                else:
                    print(-z - y - x)
        else:
            if z > 0:
                # x < 0, y < 0, z > 0
                if -x > z:
                    print(-x + y)
                else:
                    print(z + y - x)
            else:
                # x < 0, y < 0, z < 0
                if -x > -z:
                    print(-x + y)
                else:
                    print(-z + y - x)
