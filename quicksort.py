# from pylab import *
# import numpy as np
# from scipy.stats import mannwhitneyu

import numpy as np
import matplotlib as mpl
mpl.use('pgf')

def get_lines(path):
    with open(path) as f:
        lines = f.readlines()
        return np.array([int(line)/100000 for line in lines])

def get_data(path):
    return np.transpose(get_lines(path))


def figsize(scale):
    fig_width_pt = 229.5                          # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "text.fontsize": 10,
    "legend.fontsize": 10,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ],
    'image.cmap': 'gray'
    }
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt
import pylab

# I make my own newfig and savefig functions
def newfig(width):
    plt.clf()
    fig = plt.figure(figsize=figsize(width))
    ax = fig.add_subplot(111)
    return fig, ax

def savefig(filename):
    plt.savefig('{}.pgf'.format(filename))
    plt.savefig('{}.pdf'.format(filename))

#extract the appropriate column of data
old_data = get_data("oldTimes2")
static_data = get_data("staticTimes2")
reflect_data = get_data("reflectTimes2")
generic_data = get_data("genericTimes2")

#plot 1

print np.median(old_data), np.median(static_data), np.median(reflect_data), np.median(generic_data)

fig, ax = newfig(1)

bp = ax.boxplot([old_data, static_data, reflect_data, generic_data])
pylab.setp(bp['boxes'], color='black')
pylab.setp(bp['whiskers'], color='black')
pylab.setp(bp['fliers'], color='black')
pylab.setp(bp['medians'], color='gray')

# ax.set_title("Quicksort Runtimes")

ax.set_xticklabels(['Current', 'Conventional', 'Reflection', 'Generic'])
ax.set_xlabel('Implementation')

# yticks([0,1,2,3,4,5, 6, 7, 8],('0','10^1','10^2','10^3','10^4','10^5', '10^6', '10^7', '10^8'))
ax.set_ylabel('Runtime (milliseconds)')


plt.tight_layout(0.5)

savefig('quicksort2')

# def format_axes(ax):

#     for spine in ['top', 'right']:
#         ax.spines[spine].set_visible(False)

#     for spine in ['left', 'bottom']:
#         ax.spines[spine].set_color(SPINE_COLOR)
#         ax.spines[spine].set_linewidth(0.5)

#     ax.xaxis.set_ticks_position('bottom')
#     ax.yaxis.set_ticks_position('left')

#     for axis in [ax.xaxis, ax.yaxis]:
#         axis.set_tick_params(direction='out', color=SPINE_COLOR)

#     return ax

# fig_width_pt = 229.5 * 0.9  # Get this from LaTeX using \showthe\columnwidth
# inches_per_pt = 1.0/72.27               # Convert pt to inch
# golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
# fig_width = fig_width_pt*inches_per_pt  # width in inches
# fig_height = fig_width*golden_mean      # height in inches
# fig_size =  [fig_width,fig_height]
# params = {'backend': 'ps',
#           'axes.labelsize': 10,
#           'text.fontsize': 10,
#           'legend.fontsize': 10,
#           'xtick.labelsize': 8,
#           'ytick.labelsize': 8,
#           'text.usetex': True,
#           'figure.figsize': fig_size}

# #extract the appropriate column of data
# static_data = get_data("staticTimes")
# reflect_data = get_data("reflectTimes")
# generic_data = get_data("genericTimes")

# rcParams.update(params)

# #plot 1
# boxplot([static_data, reflect_data, generic_data])

# grid()

# title("Quicksort Runtimes")

# xticks([1,2,3],('Specialized', 'Reflection', 'Generic'))
# xlabel('Version')

# # yticks([0,1,2,3,4,5, 6, 7, 8],('0','10^1','10^2','10^3','10^4','10^5', '10^6', '10^7', '10^8'))
# ylabel('Runtime (milliseconds)')


# #save the plot
# # show()
# # savefig("plot.svg")

# #print mannwhitneyu(c_data[200,:],e_data[200,:])

# # Generate data
# savefig('quicksort.eps')
