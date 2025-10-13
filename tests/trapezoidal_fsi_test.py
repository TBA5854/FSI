import numpy as np
import random
import fsi
import matplotlib.pyplot as plt

# Pick random numbers a < b < c
a = random.uniform(0, 5)
b1 = random.uniform(a + 0.1, a + 5)
b2 = random.uniform(b1, a + 5)
c = random.uniform(b2 + 0.1, b2 + 5)

# Generate x values between a and c
x = np.linspace(a, c,10000)
f = [fsi.trapezoidal_fuzzer(a, b1, b2, c, xi) for xi in x]
# print(f)

plt.plot(x, f, label='fsi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Trapezoidal FSI: a={a:.2f}, b1={b1:.2f}, b2={b2:.2f}, c={c:.2f}')
plt.axvline(a, color='red', linestyle='--', label='a')
# plt.axvline(b, color='yellow', linestyle='--', label='b')
plt.axvline(c, color='green', linestyle='--', label='c')
plt.scatter([a], [fsi.trapezoidal_fuzzer(a, b1, b2, c, a)], color='red', zorder=5)
# plt.scatter([b], [fsi.trapezoidal_fuzzer(a, b1, b2, c, b)], color='yellow', zorder=5)
plt.scatter([c], [fsi.trapezoidal_fuzzer(a, b1, b2, c, c)], color='green', zorder=5)
plt.legend()
plt.grid(True)
plt.show()