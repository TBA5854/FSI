def trapezoidal_fuzzer(a: float, b1: float, b2: float, c: float, x: float) -> float:
    if not (a < b1 <= b2 < c):
        raise ValueError("Input must satisfy: a < b1 <= b2 < c")
    if x < a or x > c:
        return 0.0
    elif b1 <= x <= b2:
        return 1.0
    elif a <= x < b1:
        return (x - a) / (b1 - a)
    else:
        return (c - x) / (c - b2)