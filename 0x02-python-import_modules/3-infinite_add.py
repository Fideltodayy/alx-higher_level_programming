#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    sum_of_args = 0
    result = 0
    for arg in args:
        sum_of_args += int(arg)
    print(sum_of_args)
