from activation_functions import (
    relu,
    relu_derivative,
    sigmoid,
    sigmoid_derivative,
    tanh,
    tanh_derivative,
)
from plots_create import (
    ActivationItem,
    plot_all_activations_and_derivatives,
    single_plot,
)


def main(show: bool = True, save: bool = True):
    single_plot(func=relu, save=save, show=show)
    single_plot(func=sigmoid, save=save, show=show)
    single_plot(func=tanh, save=save, show=show)

    single_plot(func=relu_derivative, save=save, show=show)
    single_plot(func=sigmoid_derivative, save=save, show=show)
    single_plot(func=tanh_derivative, save=save, show=show)

    activation_functions: list[ActivationItem] = [
        {
            "func": sigmoid,
            "deriv_func": sigmoid_derivative,
            "color": "blue",
        },
        {"func": tanh, "deriv_func": tanh_derivative, "color": "red"},
        {"func": relu, "deriv_func": relu_derivative, "color": "green"},
    ]

    plot_all_activations_and_derivatives(
        show=show, save=save, activation_functions=activation_functions
    )


if __name__ == "__main__":
    main(show=False)
