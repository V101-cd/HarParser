import json
# import tldextract
from urllib.parse import urlsplit

class HarParser():
    def __init__(self, har_filename):
        with open(har_filename, encoding="utf8") as f: ## HAR files must be UTF8 encoded
            har = json.load(f)
            self.har_entries = har['log']['entries']
            
        self.siteOccurrences = {}
        
    def parseSites(self):
        for entry in self.har_entries:
            request_url = str(entry['request']['url'])
            # parsed_url = tldextract.extract(url=request_url, include_psl_private_domains=True)
            # site = parsed_url.subdomain + '.' + parsed_url.domain + '.' + parsed_url.suffix
            # request_url_domain_substring = request_url.split(site, 1)[0]
            parsed_url = urlsplit(request_url)
            site = request_url.split(parsed_url.netloc, 1)[0] + parsed_url.netloc
            if site != '':
                if site in self.siteOccurrences.keys():
                    self.siteOccurrences[site]['counts'] += 1
                else:
                    # self.siteOccurrences[site] = {'counts': 1, 'is_private': parsed_url.is_private}
                    self.siteOccurrences[site] = {'counts': 1}
                    
    def downloadSites(self, output_path="."):
        with open(f"{output_path}/yamahamusiclondon-sitesandcount.csv", 'w') as f:
            # f.write('Site/file, Count, Private domain?\n')
            f.write('Site/file, Count\n')
            print(self.siteOccurrences.keys())
            for site, site_metrics in sorted(self.siteOccurrences.items()):
                # f.write(','.join(map(str, [site, site_metrics['counts'], site_metrics['is_private']])) + '\n')
                f.write(','.join(map(str, [site, site_metrics['counts']])) + '\n')
                # add column for HAR line
        print("Sites downloaded")

    # def getSites(self):
    #     self.parseSites()
    #     sites = self.siteOccurrences
    #     return sites
    
    # def getUniqueSiteCounts(self):
    #     self.parseSites()
    #     return self.siteOccurrences()
    
har_path = "C:/Users/vspar/Documents/Vedika Homework/Uni/CS/Year 5/Cyber Security/Take 2/www.yamahamusiclondon.com.har"
harparser = HarParser(har_path)
harparser.parseSites()
harparser.downloadSites()