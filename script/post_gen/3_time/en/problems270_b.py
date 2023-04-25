Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if z > y:
        print(x - z)
    else:
        print(-1)

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        print(-1)
    else:
        print(X - Z)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    X, Y, Z = map(int, input().split())
    if X > 0 and Y > 0:
        if X < Y:
            print(X - Z)
        else:
            print(X)
    elif X > 0 and Y < 0:
        print(X - Z)
    elif X < 0 and Y > 0:
        print(Y - Z)
    elif X < 0 and Y < 0:
        if X < Y:
            print(X - Z)
        else:
            print(Y - Z)
    else:
        print(-1)

=======
Suggestion 5

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        print(-1)
    else:
        print(Z + Y)

=======
Suggestion 6

def main():
    X, Y, Z = map(int, input().split())
    if X < Z and Z < Y:
        print(abs(X-Y))
    else:
        print(-1)

=======
Suggestion 7

def main():
    x, y, z = map(int, input().split())
    if y < z:
        print(-1)
        return
    print(abs(x))

=======
Suggestion 8

def main():
    x,y,z = map(int,input().split())
    if z < y:
        print(x-z)
    else:
        print(-1)

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    #Get input
    x,y,z = map(int, input().split())
    #Calculate distance to goal
    dist_goal = abs(x)
    #Calculate distance to hammer
    dist_hammer = abs(z)
    #Calculate distance to wall
    dist_wall = abs(y)
    #If hammer is before wall, then go get the hammer
    if dist_hammer < dist_wall:
        #Calculate distance to hammer and back
        dist_hammer = dist_hammer + dist_hammer
        #Calculate total distance
        dist_total = dist_hammer + dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is after wall, then go to goal
    elif dist_hammer > dist_wall:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at wall, then go to goal
    elif dist_hammer == dist_wall:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at goal, then go to goal
    elif dist_hammer == dist_goal:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at origin, then go to goal
    elif dist_hammer == 0:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If goal is at origin, then go to hammer
    elif dist_goal == 0:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer and goal are at the same location, then go to hammer
    elif dist_goal == dist_hammer:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer and goal are at the same location, then go to hammer
    elif dist_goal == dist_hammer:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer is at wall, then go to goal
    elif dist_hammer == dist_wall:
        #Calculate total distance
        dist_total = dist
