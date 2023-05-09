def main():
    import sys
    N,A,B = map(int, sys.stdin.readline().strip().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2 == 0:
                        sys.stdout.write('.')
                    else:
                        sys.stdout.write('#')
                sys.stdout.write('\n')
        sys.stdout.write('\n')
