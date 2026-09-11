import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# Mapping PWM to time (s) it took for car to traverse 1 meter
test_data = {
    25: [5.23, 5.29, 5.26, 5.3, 5.26],
    30: [4.1, 4.11, 4.09, 4.02, 4.23],
    35: [3.4, 3.36, 3.44, 3.51, 3.51],
    50: [2.31, 2.36, 2.37, 2.4, 2.36],
    75: [1.47, 1.41, 1.4, 1.54, 1.51],
    100: [1.18, 1.13, 1.13, 1.19, 1.14]
}

x = []
y = []

for pwm, times in test_data.items():
    x.append(pwm)
    y.append(np.mean(times))

x, y = np.array(x), np.array(y)

print(Polynomial.fit(x, y, 2))
# y_pred = m * x + c

# plt.xlabel("PWM")
# plt.ylabel("Time (s)")
# plt.title("Time to Traverse 1 Meter vs PWM")
# plt.plot(x,y, 'o-', label="Average Time")
# plt.plot(x, y_pred, 'o-', label="Predicted Time")

# plt.legend()
# plt.show()