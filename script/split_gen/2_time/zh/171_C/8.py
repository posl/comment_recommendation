def dog_name(n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    length = len(alpha)
    if n <= length:
        return alpha[n-1]
    else:
        n -= length
        n -= 1
        if n < length:
            return alpha[n]
        else:
            n -= length
            n -= 1
            if n < length * length:
                return alpha[n // length] + alpha[n % length]
            else:
                n -= length * length
                n -= 1
                if n < length * length * length:
                    return alpha[n // (length * length)] + alpha[n // length % length] + alpha[n % length]
                else:
                    n -= length * length * length
                    n -= 1
                    if n < length * length * length * length:
                        return alpha[n // (length * length * length)] + alpha[n // (length * length) % length] + alpha[n // length % length] + alpha[n % length]
                    else:
                        n -= length * length * length * length
                        n -= 1
                        if n < length * length * length * length * length:
                            return alpha[n // (length * length * length * length)] + alpha[n // (length * length * length) % length] + alpha[n // (length * length) % length] + alpha[n // length % length] + alpha[n % length]
                        else:
                            n -= length * length * length * length * length
                            n -= 1
                            if n < length * length * length * length * length * length:
                                return alpha[n // (length * length * length * length * length)] + alpha[n // (length * length * length * length) % length] + alpha[n // (length * length * length) % length] + alpha[n // (length * length) % length] + alpha[n // length % length] + alpha[n % length]
                            else:
                                n -= length * length * length * length * length * length
                                n -= 1
                                if n < length * length * length * length * length * length * length:
                                    return alpha[n // (length * length * length * length * length * length)] + alpha[n // (length * length * length * length * length) % length] + alpha[n // (length * length * length * length) % length] +
