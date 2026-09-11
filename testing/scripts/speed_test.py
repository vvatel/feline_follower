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

def convert_time_to_speed(input_time):
    return 1 / input_time

if __name__ == '__main__':
    x = []
    y = []

    


    for pwm, times in test_data.items():
        x.append(pwm)
        y.append(
            convert_time_to_speed(np.mean(times))
        )

    x, y = np.array(x), np.array(y)

    forward_pred = Polynomial.fit(x, y, 3)
    inverse_pred = Polynomial.fit(y, x, 3)

    plt.xlabel("PWM (%)")
    plt.ylabel("Speed (m/s)")
    plt.plot(x,y, 'o-', label="Average")

    x_pred = np.arange(25,100)
    plt.plot(x_pred, forward_pred(x_pred), '--', label="Predicted")

    plt.legend()
    plt.show()
