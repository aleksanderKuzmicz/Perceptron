"""
Perceptron from scratch

* weighted_sum
* activation function (sign activation function)

"""


class Perceptron:
    def __init__(self, num_inputs=2, weights=(2, 1)):
        """Initiates perceptron

        :param num_inputs: Each input corresponds to a feature.
        :type num_inputs: int
        :param weights: Each input has a weights which assigns a certain amount of importance to the input.
        :type weights: list
        """
        self._num_inputs = num_inputs
        self._weights = weights

    def weighted_sum(self, inputs):
        """Calculate and return weighted sum of the inputs

        :param inputs: Input values to perceptron
        :type inputs: list
        :return: Weighted sum of the inputs
        :rtype: float
        """
        assert len(inputs) == self._num_inputs, f"Input size ({len(inputs)}) is not equal to object's inputs " \
                                               f"({self._num_inputs})"
        weighted_sum = 0
        for i in range(self._num_inputs):
            weighted_sum += self._weights[i] * inputs[i]

        return weighted_sum

    def activation(self, weighted_sum):
        """Sign activation function

        :param weighted_sum: Weighted sum of the inputs
        :type weighted_sum: float
        :return: 1 if weighted_sum is greater or equal to 0.
        :rtype: int
        """
        if weighted_sum >= 0:
            return 1
        else:
            return -1
