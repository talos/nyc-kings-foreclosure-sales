#!/usr/bin/env python

import requests
import bs4
import urlparse
import time
import os
import sys
from dateutil import parser


COURT_URL = 'http://www.nycourts.gov/courts/2jd/kings/civil/foreclosuresales.shtml'
OUTPUT_DIR = 'output'
CHUNK_SIZE = 1024

def main():
  if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

  session = requests.session()

  resp = session.get(COURT_URL)
  soup = bs4.BeautifulSoup(resp.text)

  for pdf_link in soup.select('a[href$=".pdf"]'):
    title = pdf_link.text
    sys.stderr.write(u'{}:\n'.format(title))
    pdf_url = urlparse.urljoin(COURT_URL, pdf_link.get('href'))
    pdf_resp = session.get(pdf_url, stream=True)

    last_modified = pdf_resp.headers['Last-Modified']
    timestamp = int(time.mktime(parser.parse(last_modified).timetuple()))
    file_path = os.path.join(OUTPUT_DIR, u'{}_{}.pdf'.format(timestamp, title))
    #file_path = os.path.join(OUTPUT_DIR, pdf_url.split('/')[-1])

    if os.path.exists(file_path):
      sys.stderr.write('skipping\n')
      continue

    with open(file_path, 'wb') as fd:
      sys.stderr.write('downloading\n')
      for chunk in pdf_resp.iter_content(CHUNK_SIZE):
        fd.write(chunk)

    #time.sleep(1)

if __name__ == '__main__':
  main()
