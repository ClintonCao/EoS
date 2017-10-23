import json
import tldextract
from collections import Counter

bing = None
with open('bing_results2.txt') as f:
    bing = json.loads(f.read())

BLOCK = 10000

mini = min(bing.values())
maxi = max(bing.values())
# 0 4.810.000.000

print mini, maxi

print len(bing.values())

print len(filter(lambda x: x == 0, bing.values()))

counts = Counter(map(lambda x: x / BLOCK, bing.values()))
print sorted(counts.iteritems(), key=lambda x: x[0])

scores = {}
with open('virustotal_report.txt') as f:
    vtscores = f.read().split('\n')
    for vtscore in vtscores:
        url, score = vtscore.rsplit(':', 1)
        score = score.strip()
        scores.update({url: score})

grid = {}

for url, score in scores.iteritems():
    extract = tldextract.extract(url)
    domain = extract.domain + '.' + extract.suffix
    result = bing[domain]
    key = (score, result / BLOCK)
    count = grid.setdefault(key, 0)
    grid[key] = count + 1

print filter(lambda x: int(x[0][0]) <= 12 and x[0][1] <= 12, sorted(grid.items(), key=lambda x: x[0]))
