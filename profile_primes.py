#!/usr/bin/env python
import sys
from line_profiler import LineProfiler


if __name__ == '__main__':
    filename = sys.argv[1]

    profiler = LineProfiler()
    profiler.runctx(
        'execfile(%r, globals())' % (filename,), locals(), locals())
    profiler.print_stats()
