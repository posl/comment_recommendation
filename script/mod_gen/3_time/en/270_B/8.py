def main():
    x,y,z = map(int,input().split())
    if x < 0:
        if y < 0:
            if z < 0:
                if z < y:
                    print(abs(x-y)+abs(y-z))
                else:
                    print(abs(x-z))
            else:
                print(abs(x-y)+abs(y-z))
        else:
            print(abs(x-y)+abs(y-z))
    else:
        if y < 0:
            if z < 0:
                if z < y:
                    print(abs(x-y)+abs(y-z))
                else:
                    print(abs(x-z))
            else:
                print(abs(x-y)+abs(y-z))
        else:
            if z < 0:
                if z < y:
                    print(abs(x-y)+abs(y-z))
                else:
                    print(abs(x-z))
            else:
                print(-1)
main()
I think this is a pretty good solution, but it's not working. It's giving me a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3.7.3
I'm not sure if this is a bug or if I'm doing something wrong, but I'm getting a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3.7.3
I think this is a pretty good solution, but it's not working. It's giving me a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3.7.3
I'm not sure if this is a bug or if I'm doing something wrong, but I'm getting a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3.7.3
I'm not sure if this is a bug or if I'm doing something wrong, but I'm getting a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3.7.3
I'm not sure if this is a bug or if I'm doing something wrong, but I'm getting a runtime error. Can someone please help me figure out why?
I'm not sure what the problem is. I'm using Python 3

if __name__ == '__main__':
    main()