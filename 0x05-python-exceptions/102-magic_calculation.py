#!/usr/bin/python3


def magic_calculation(a, b):
    counter = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            counter += a ** b / i
        except:
            result = b + a
            break

    return result
