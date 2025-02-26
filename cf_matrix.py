from typing import List

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def make_confusion_matrix(cf,
                          group_names: List[str] = None,
                          categories: List[str] = 'auto',
                          count: bool = True,
                          percent: bool = True,
                          cbar: bool = True,
                          xy_ticks: bool = True,
                          xy_plot_labels: bool = True,
                          sum_stats: bool = True,
                          fig_size: bool = None,
                          cmap: str = 'Blues',
                          title: str = None,
                          mask: np.ndarray = None):
    """
    This function will make a pretty plot of a sklearn Confusion Matrix cm using a Seaborn heatmap visualization.

    Arguments
    ---------
    cf:            confusion matrix to be passed in

    group_names:    List of strings that represent the labels row by row to be shown in each square.

    categories:     List of strings containing the categories to be displayed on the x,y axis. Default is 'auto'

    count:          If True, show the raw number in the confusion matrix. Default is True.

    percent:        If True, show the proportions for each category. Default is True.

    cbar:           If True, show the color bar. The cbar values are based off the values in the confusion matrix.
                    Default is True.

    xy_ticks:       If True, show x and y ticks. Default is True.

    xy_plot_labels: If True, show 'True Label' and 'Predicted Label' on the figure. Default is True.

    sum_stats:      If True, display summary statistics below the figure. Default is True.

    fig_size:       Tuple representing the figure size. Default will be the matplotlib rcParams value.

    cmap:           Colormap of the values displayed from matplotlib.pyplot.cm. Default is 'Blues'
                    See https://matplotlib.org/examples/color/colormaps_reference.html

    title:          Title for the heatmap. Default is None.

    mask:           Binary mask for confusion matrix (True means to show cell of matrix, False means not)
    """

    # CODE TO GENERATE TEXT INSIDE EACH SQUARE
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten() / np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels, group_counts, group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        # Accuracy is sum of diagonal divided by total observations
        accuracy = np.trace(cf) / float(np.sum(cf))

        # if it is a binary confusion matrix, show some more stats
        if len(cf) == 2:
            # Metrics for Binary Confusion Matrices
            precision = cf[1, 1] / sum(cf[:, 1])
            recall = cf[1, 1] / sum(cf[1, :])
            f1_score = 2 * precision * recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy, precision, recall, f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""

    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if fig_size is None:
        # Get default figure size if not set
        fig_size = plt.rcParams.get('figure.fig_size')

    if xy_ticks is False:
        # Do not show categories if xy_ticks is False
        categories = False

    # MAKE THE HEATMAP VISUALIZATION
    plt.figure(figsize=fig_size)

    sns.heatmap(cf,
                annot=box_labels,
                fmt="",
                cmap=cmap,
                cbar=cbar,
                xticklabels=categories,
                yticklabels=categories,
                mask=mask)

    if xy_plot_labels:
        plt.ylabel('True label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)

    if title:
        plt.title(title)
