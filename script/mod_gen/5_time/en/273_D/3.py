def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = []
    for i in range(n):
        walls.append(list(map(int, input().split())))
    q = int(input())
    instructions = []
    for i in range(q):
        instructions.append(list(input().split()))
    #print(h, w, rs, cs)
    #print(walls)
    #print(q)
    #print(instructions)
    #print()
    #print('initial')
    #print('h: ', h)
    #print('w: ', w)
    #print('rs: ', rs)
    #print('cs: ', cs)
    #print('walls: ', walls)
    #print('q: ', q)
    #print('instructions: ', instructions)
    for i in range(len(instructions)):
        #print()
        #print('i: ', i)
        #print('h: ', h)
        #print('w: ', w)
        #print('rs: ', rs)
        #print('cs: ', cs)
        #print('walls: ', walls)
        #print('q: ', q)
        #print('instructions: ', instructions)
        #print('instructions[i]: ', instructions[i])
        #print('instructions[i][0]: ', instructions[i][0])
        #print('instructions[i][1]: ', instructions[i][1])
        #print('instructions[i][0] == "L": ', instructions[i][0] == "L")
        #print('instructions[i][0] == "R": ', instructions[i][0] == "R")
        #print('instructions[i][0] == "U": ', instructions[i][0] == "U")
        #print('instructions[i][0] == "D": ', instructions[i][0] == "D")
        #print('instructions[i][0] == "L" and cs > 1: ', instructions[i][0] == "L" and cs > 1)
        #print('instructions[i][0] == "R" and cs < w: ', instructions[i][0] == "R" and cs < w)
        #print('instructions[i][0] == "U" and rs > 1: ', instructions[i][0] == "U" and rs > 1)
        #print('instructions[i][

if __name__ == '__main__':
    main()