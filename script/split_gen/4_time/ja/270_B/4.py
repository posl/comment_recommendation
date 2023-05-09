def main():
    x, y, z = map(int, input().split())
    if x > 0 and y > 0 and z > 0:
        if x > y:
            print(x - y + z)
        else:
            print(z - y + x)
    elif x > 0 and y < 0 and z < 0:
        if x > -y:
            print(x - -y + -z)
        else:
            print(-z - -y + x)
    elif x < 0 and y < 0 and z < 0:
        if -x > -y:
            print(-x - -y + -z)
        else:
            print(-z - -y + -x)
    elif x < 0 and y > 0 and z > 0:
        if -x > y:
            print(-x - y + z)
        else:
            print(z - y + -x)
    elif x > 0 and y > 0 and z < 0:
        if x > y:
            print(x - y + -z)
        else:
            print(-z - y + x)
    elif x > 0 and y < 0 and z > 0:
        if x > -y:
            print(x - -y + z)
        else:
            print(z - -y + x)
    elif x < 0 and y < 0 and z > 0:
        if -x > -y:
            print(-x - -y + z)
        else:
            print(z - -y + -x)
    elif x < 0 and y > 0 and z < 0:
        if -x > y:
            print(-x - y + -z)
        else:
            print(-z - y + -x)
    else:
        print(-1)
