import urllib2
import re
import tldextract
import json

from malware_domains import get_attribute_values, DOMAIN

# traffic = 'http://www.siteworthtraffic.com/report/%s'
traffic = 'https://www.bing.com/search?q=%s'

# domains = ['finnhair.co.uk', 'directxex.com', 'resolvethem.com']
domains = get_attribute_values(DOMAIN)
values = {}
tlds = {}


for _domain in domains:
    _domain = _domain.strip()
    if _domain in ('', '-'):
        continue
    extract = tldextract.extract(_domain)
    domain = extract.domain + '.' + extract.suffix

    tldcount = tlds.setdefault(extract.suffix, 0)
    tlds[extract.suffix] = tldcount + 1

    if domain in values:
        continue

    url = traffic % domain
    print url
    try:
        result = urllib2.urlopen(url).read()
        '''
        if 'MONTHLY ESTIMATIONS' in result:
            relevant = result.split('MONTHLY ESTIMATIONS')[1]
            relevant = relevant.split('YEARLY ESTIMATIONS')[0]
            match = re.search(r'<td>Unique Pageviews</td> <td>([\d+,*]+)</td>', relevant)
            if match:
                try:
                    str_value = match.group(1).strip().replace(',', '')
                    value = int(str_value)
                except:
                    value = 0
            else:
                value = 0
        else:
            value = 0
        '''
        'class="sb_count">43.500 Resultaten'
        match = re.search(r'class="sb_count">([\d.]+) Result', result)
        if match:
            try:
                str_value = match.group(1).strip().replace(',', '').replace('.', '')
                value = int(str_value)
            except:
                value = 0
        else:
            value = 0
    except:
        value = 0

    values[domain] = value

print values
with open('bing_results2.txt', 'w') as f:
    f.write(json.dumps(values))
