import numpy as np
import random
import fsi
import matplotlib.pyplot as plt

# Pick random numbers a < b < c
a = random.uniform(0, 5)
b = random.uniform(a + 0.1, a + 5)
c = random.uniform(b + 0.1, b + 5)

# Generate x values between a and c
x = np.linspace(a, c,10000)
f = [fsi.triangular_fuzzer(a, b, c, xi) for xi in x]
print(f)

plt.plot(x, f, label='fsi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Triangular FSI: a={a:.2f}, b={b:.2f}, c={c:.2f}')
plt.axvline(a, color='red', linestyle='--', label='a')
# plt.axvline(b, color='yellow', linestyle='--', label='b')
plt.axvline(c, color='green', linestyle='--', label='c')
plt.scatter([a], [fsi.triangular_fuzzer(a, b, c, a)], color='red', zorder=5)
# plt.scatter([b], [fsi.triangular_fuzzer(a, b, c, b)], color='yellow', zorder=5)
plt.scatter([c], [fsi.triangular_fuzzer(a, b, c, c)], color='green', zorder=5)
plt.legend()
plt.grid(True)
plt.show()