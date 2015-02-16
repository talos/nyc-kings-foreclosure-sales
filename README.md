# Preserve Foreclosure Sale PDFs posted to the Kings County Supreme Court

This script preserves the PDFs posted to the [Kings County Supreme Court][].

  [Kings County Supreme Court]: http://www.nycourts.gov/courts/2jd/kings/civil/foreclosuresales.shtml 

Archives going forward are accessible here:


### Installation

Preferably inside a virtualenv:

    pip install -r requirements.txt

### Usage

With the virtualenv activated, executing the script will save output in
a folder called `output`.

    ./download.py

### TODO

* OCR
* Automatic posting to [data.beta.nyc][]

  [data.beta.nyc]: http://data.beta.nyc
