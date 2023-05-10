def main():
    input = raw_input()
    input = input.split()
    N = int(input[0])
    A = int(input[1])
    B = int(input[2])
    for i in range(0,N):
        for j in range(0,A):
            for k in range(0,N):
                if (i+j)%2==0:
                    for l in range(0,B):
                        print ".",
                else:
                    for l in range(0,B):
                        print "#",
            print ""
    return 0
