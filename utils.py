from matplotlib import pyplot as plt
import numpy as np


class Utils:

    @staticmethod
    def create_plot(f, x_range: tuple[int, int]=(-5, 5),
                    num_points:int =500,
                    figsize: tuple[int, int]=(10, 10),
                    label: str='f(x) = x^3 - 2x + 4'):
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = [f(xn) for xn in x] 
        
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(x, y, label=label)
        ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
        ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid()


    @staticmethod
    def draw_plots(data):
        plt.figure(figsize=(10, 10))

        for x_range, y_range, label in data:
            plt.plot(x_range, y_range, label=label)
        
        plt.axhline(0, color='black', linewidth=1, linestyle='-')
        plt.axvline(0, color='black', linewidth=1, linestyle='-')
        plt.grid()
        plt.legend()
        