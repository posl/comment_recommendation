def main():
    N = int(input())
    #N = 5
    #N = 4
    #N = 10
    #print(N)
    #a = [1, 2, 3, 4]
    #b = [4, 4, 4, 5]
    #a = [2, 1, 2]
    #b = [4, 4, 3]
    a = [9, 3, 4, 8, 1, 2, 7, 6, 5]
    b = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    #print(a)
    #print(b)
    #print(len(a))
    #print(len(b))
    count = 0
    for i in range(len(a)):
        if a[i] == 1 or b[i] == 1:
            count += 1
    if count == 1:
        print("Yes")
    else:
        print("No")
main()
I'm not sure what you mean by "directly connected", but if you mean that there is a unique path between every pair of vertices, then that is not necessarily the case. Consider the following graph:
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9
This is a star, but there is no unique path between every pair of vertices.
I'm not sure what you mean by "directly connected", but if you mean that there is a unique path between every pair of vertices, then that is not necessarily the case. Consider the following graph: 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 This is a star, but there is no unique path between every pair of vertices.
I'm sorry for my poor English. I mean that there is a vertex directly connected to all other vertices.
I'm sorry for my poor English. I mean that there is a vertex directly connected to all other vertices.
Ah, that makes more sense. In that case, you can use the following algorithm:
Let v be the vertex that is directly connected to all other vertices.
Let E be the set of edges in the graph.
Let V be the set of vertices in the graph.

if __name__ == '__main__':
    main()