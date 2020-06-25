from matplotlib import pyplot as plt
from output import DATA


def create_figure() -> None:
    x_values = list(DATA.keys())
    y_values = list(DATA.values())

    plt.bar(x_values, y_values)
    plt.xticks(rotation=30)
    
    plt.show()


if __name__ == '__main__':
    create_figure()

