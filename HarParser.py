import json
import sys
from urllib.parse import urlsplit

class HarParser():
    def __init__(self, har_filename, output_filename="harparser-sites_and_counts.csv"):
        with open(har_filename, encoding="utf8") as f: ## HAR files must be UTF8 encoded
            har = json.load(f)
            self.har_entries = har['log']['entries']
            
        self.siteOccurrences = {}
        if output_filename.endswith('.csv') == False:
            self.output_filename = output_filename + '.csv'
        else:
            self.output_filename = output_filename
        
    def parseSites(self):
        for entry in self.har_entries:
            request_url = str(entry['request']['url'])
            parsed_url = urlsplit(request_url)
            site = request_url.split(parsed_url.netloc, 1)[0] + parsed_url.netloc
            if site != '':
                if site in self.siteOccurrences.keys():
                    self.siteOccurrences[site]['counts'] += 1
                else:
                    self.siteOccurrences[site] = {'counts': 1}
                    
    def downloadSites(self, output_path="."):
        with open(f"{output_path}/{self.output_filename}", 'w') as f:
            f.write('Site/file, Count\n')
            print(self.siteOccurrences.keys())
            for site, site_metrics in sorted(self.siteOccurrences.items()):
                f.write(','.join(map(str, [site, site_metrics['counts']])) + '\n')
        print("Sites downloaded")
    
har_path = sys.argv[1]
output_filename = sys.argv[2]
harparser = HarParser(har_path, output_filename)
harparser.parseSites()
harparser.downloadSites()