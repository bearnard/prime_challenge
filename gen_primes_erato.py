@profiler
def prime_erato(num):

    arr = dict((x, True) for x in xrange(2, num + 1))

    for x in xrange(2, int(num ** 0.5) + 1):
        if arr[x]:
            for j in range(x * x, num + 1, x):
                if j > num:
                    break
                arr[j] = False

    return [x for x, y in arr.iteritems() if y]


prime_erato(100000)
