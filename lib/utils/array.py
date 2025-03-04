def array_slice(xs, n):
    n = max(1, n)
    return list(xs[i:i+n] for i in range(0, len(xs), n))

def array_merge(one, two):
    return one + two