import requests
import sys
import time
from malware_domains import get_attribute_values, DOMAIN

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Specify a part between 0 and 5'
        sys.exit()

    try:
        part = int(sys.argv[1])
    except:
        print 'Part not an integer'
        sys.exit()
    if part < 0 or part > 5:
        print 'Part not between 0 and 5'
        sys.exit()

    domains = get_attribute_values(DOMAIN)
    size = len(domains)
    parts_size = size / 6
    domains = domains[part * parts_size: None if part == 5 else (part + 1) * parts_size]

    SHARIF_API_KEY1 = '9e390226d782b837cfdfbc77b8c77bc60185f966d08993fb365e569b1f893bdb'
    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    limit = None
    succes = 0

    results = []

    for i, domain in enumerate(domains):
        try :
            if limit and succes >= limit:
                break
            if domain in ('-', ''):
                continue
            if succes > 0 and succes % 4 == 0:
                print '(%d/%d)...' % (i, parts_size)
                time.sleep(61)
            params = {'apikey': SHARIF_API_KEY1, 'resource': domain}
            response = requests.get(url, params=params)
            json_response = response.json()
            result = '%s: %d' % (domain, json_response['positives'])
            results.append(result)
            print result
            succes += 1
        except:
            break

    with open('2virustotal_report_%d.txt' % part, 'w') as f:
        for result in results:
            f.write('%s\n' % result)
