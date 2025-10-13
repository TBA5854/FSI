def triangular_fuzzer(a: float, b1: float, c: float, x: float) -> float:
    if not (a < b1 < c):
        raise ValueError("Input must satisfy: start < b1 < end")
    if x < a or x > c:return 0
    else:
        if x==b1:return 1
        elif x < b1:
            return (x - a) / (b1 - a)
        else:
            return (c - x) / (c - b1)
        