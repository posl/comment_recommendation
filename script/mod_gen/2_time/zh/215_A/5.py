def get_max_weight(edges, u, v):
    if u == v:
        return 0
    else:
        max_weight = 0
        for e in edges:
            if (e[0] == u and e[1] == v) or (e[0] == v and e[1] == u):
                if e[2] > max_weight:
                    max_weight = e[2]
                    break
        for e in edges:
            if e[0] == u:
                weight = get_max_weight(edges, e[1], v)
                if weight > max_weight:
                    max_weight = weight
            elif e[1] == u:
                weight = get_max_weight(edges, e[0], v)
                if weight > max_weight:
                    max_weight = weight
        return max_weight

if __name__ == '__main__':
    get_max_weight()