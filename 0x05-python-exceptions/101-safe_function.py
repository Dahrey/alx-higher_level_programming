#!/usr/bin/python3
def magic_calculation(a, b):
    fresult = 0
    for f in range(1, 3):
        try:
            if f > a:
                raise Exception('Too far')
            fresult += a ** b / f
        except Exception:
            fresult = b + a
            break
    return fresult
