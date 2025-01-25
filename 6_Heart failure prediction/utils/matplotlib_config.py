"""
This module contains the configuration for the matplotlib library.
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define the style of the plots
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    "#660000", # Blood red
    "#283618", # Dark jungle green
    "#a4ac86", # Greenish gray
    "#22577a" # Dark cerulean
])

# Define the font type
plt.rcParams['font.family'] = 'Verdana'

# Define custom map colors
# Sequential diverging colormap
seq_cmap_colors = ['#283618', 'whitesmoke', '#660000']
seq_cmap_name = 'Custom_Seq_Diverging'
custom_cmap_s = mcolors.LinearSegmentedColormap.from_list(seq_cmap_name, seq_cmap_colors)
# Register the custom colormap
plt.register_cmap(name=seq_cmap_name, cmap=custom_cmap_s)
# Qualitative colormap
qual_cmap_colors = ['#660000', '#283618', '#05668d', '#f9a620', '#81667a', '#eee82c']
qual_cmap_name = 'Custom_Qualitative'
custom_cmap_q = mcolors.ListedColormap(qual_cmap_colors, name=qual_cmap_name)
# Register the custom colormap
plt.register_cmap(name=qual_cmap_name, cmap=custom_cmap_q)
# Sequential single-hue colormap with the primary color (purple)
custom_cmap_p = mcolors.LinearSegmentedColormap.from_list(seq_cmap_name, ['#660000', 'whitesmoke'])
seq_p_cmap_name = 'Custom_Red'
# Register the custom colormap
plt.register_cmap(name=seq_p_cmap_name, cmap=custom_cmap_p)
# Sequential single-hue colormap with the primary color (purple)
custom_cmap_p_r = mcolors.LinearSegmentedColormap.from_list(seq_cmap_name, ['whitesmoke', '#660000'])
seq_p_r_cmap_name = 'Custom_Red_r'
# Register the custom colormap
plt.register_cmap(name=seq_p_r_cmap_name, cmap=custom_cmap_p_r)
"""
# Test the custom colormap
if __name__ == '__main__':
    import numpy as np
    import seaborn as sns

    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 6))
    # Create a random 2D array
    data = np.random.rand(10, 10)
    # Plot the data with the custom colormap
    sns.heatmap(data, cmap=seq_cmap_name, ax=ax)
    # Show the plot
    plt.show()
"""