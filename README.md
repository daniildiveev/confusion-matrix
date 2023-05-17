# cf_matrix.py

This file contains a function called make_confusion_matrix which can be used to create a useful visualzation of a Confusion Matrix passed in as a two dimensional numpy array.


# Docstring
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
# confusion_matrix
