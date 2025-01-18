import matplotlib.pyplot as plt


def clip(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


def pseudo_sigmoid(x: float) -> float:
    """
    :param x: float value in range [0, 1]
    :return:
    """

    if x < 0.5:
        return 2 * x * x
    else:
        return 1 - 2 * (1 - x) * (1 - x)


def dialog(actor1: float, actor2: float, changing_factor: float = .5) -> tuple:
    actor1_power = abs(0.5 - actor1) * 2
    actor2_power = abs(0.5 - actor2) * 2

    actor1_mean_repr: float = .5 - actor1
    actor2_mean_repr: float = .5 - actor2

    new_actor1: float = actor1 - changing_factor * actor2_mean_repr * pseudo_sigmoid(1 - actor1_power)
    new_actor2: float = actor2 - changing_factor * actor1_mean_repr * pseudo_sigmoid(1 - actor2_power)

    new_actor1: float = clip(new_actor1, 0.0, 1.0)
    new_actor2: float = clip(new_actor2, 0.0, 1.0)

    return new_actor1, new_actor2


def set_configuration(xlabel: str, ylabel: str, big_legend: bool = True):
    plt.grid(True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if big_legend:
        plt.legend(loc='best', fontsize=16)
    else:
        plt.legend(loc='best')