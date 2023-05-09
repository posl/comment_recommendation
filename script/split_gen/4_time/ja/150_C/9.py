def get_permutation(n):
    result = []
    def _get_permutation(n, tmp):
        if len(tmp) == n:
            result.append(tmp)
            return
        for i in range(1, n+1):
            if i in tmp:
                continue
            _get_permutation(n, tmp + [i])
    _get_permutation(n, [])
    return result
import itertools
