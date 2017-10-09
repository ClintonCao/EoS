import pylab as pl
import numpy as np
from collections import Counter


def bar_chart_dictionary(dct):
    # makes a barchart from all the items in the dictionary
    X = np.arange(len(dct))
    items = sorted(dct.items(), key=lambda x: int(x[0]))
    keys = [x[0] for x in items]
    values = [x[1] for x in items]
    pl.bar(X, values, align='center', width=.25)
    pl.xticks(X, keys)
    ymax = max(values) + 1
    pl.ylim(0, ymax)
    pl.show()


data = None
with open('virustotal_report.txt') as f:
    data = f.read().split('\n')


scores = []
for entry in data:
    score = entry.split(':')[-1].strip()
    scores.append(score)

score_count = Counter(scores)

bar_chart_dictionary(score_count)
