"""
A loss function measures how good our predictions are,
we can use this to adjust the parameters of our network
"""
import numpy as np

from nnnet.tensor import Tensor

class Loss:
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        raise NotImplementedError

    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        raise NotImplementedError


class TSE(Loss):
    
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        return np.sum((predicted - actual) ** 2)

    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return 2 * (predicted - actual)
