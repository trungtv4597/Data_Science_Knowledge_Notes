import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def frequency_table(series):
    """
    * Return a table with features:
        _frequency
        _relative frequency
        _cummulative frequency
    * Parameter:
        _Series"""
    
    frame = series.value_counts()
    frame = frame.reset_index()
    frame['relative_f'] = frame[frame.columns[1]] / frame[frame.columns[1]].sum()
    frame['cummulative_f'] = frame['relative_f'].cumsum()
    return frame


def pareto_plot(series, title=None, show_pct_y=False, pct_format='{0:.0%}', ro_degree=None, fig_size=None):
    """
    * Plot Pareto-diagrams
    * Parameter: distribution frequency table
        _frequency
        _relative frequency
        _cummulative frequency
    """
    frame = frequency_table(series)
    categories = frame[frame.columns[0]]
    frequency = frame[frame.columns[1]]
    cummulative_f = frame['cummulative_f']

    # Bar charts
    fig = plt.figure(figsize=fig_size)
    ax1 = fig.add_subplot()
    ax1.bar(categories, frequency)
    plt.title('{}'.format(title))
    plt.xticks(rotation= ro_degree)                    

    # Cummulative curve
    ax2 = ax1.twinx()
    ax2.plot(categories, cummulative_f*100, color='r', marker='D')
    ax2.yaxis.set_major_formatter(PercentFormatter())
    formatted_weights = [pct_format.format(x) for x in cummulative_f]
    for i, txt in enumerate(formatted_weights):
        ax2.annotate(txt, (categories[i], cummulative_f[i]*100), fontweight='heavy')
    
    plt.tight_layout()
    plt.show()


def get_stats(group):
    return {'fre': group.count(),
            'mean': group.mean(),
            'min': group.min(),
            'max': group.max(),
           }


def bucket_table(series, bins=10, plot=False):
    """
    * Calucate frequency distribution tables for numerical vairables.
    * Parameters:
        _Series
        _bins: numer of buckets
    """
    factor = pd.cut(series, bins)
    grouped = series.groupby(factor)
    frame = grouped.apply(get_stats).unstack()
    frame['rel_fre'] = frame['fre']  / frame['fre'].sum()
    if plot:
        frame['rel_fre'].plot.barh()
    else:
        return frame