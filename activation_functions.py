import numpy as np
from numpy.typing import NDArray


def relu(x: NDArray) -> NDArray:
    return np.maximum(x, 0)


def sigmoid(x: NDArray) -> NDArray:
    return 1 / (1 + np.exp(-x))


def tanh(x: NDArray) -> NDArray:
    return np.tanh(x)


def sigmoid_derivative(x: NDArray) -> NDArray:
    s = sigmoid(x)
    return s * (1 - s)


def tanh_derivative(x: NDArray) -> NDArray:
    return 1.0 - np.tanh(x) ** 2


def relu_derivative(x: NDArray) -> NDArray:
    return (x > 0).astype(int)
