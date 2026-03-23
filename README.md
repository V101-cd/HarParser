# HarParser
HAR (HTTP Archive) file parser, built in Python.

Extracts unique sites involved in requests captured in the HAR file, and stores these in a CSV file. The number of requests involving each unique site is also stored in the CSV file.

## Install
Download the repo, and ensure you're in the repo directory. Run:

```
pip install requirements.txt
```

## Usage
Run `python HarParser.py {path_to_har_file} {output_csv_filename}`

- replace _path_to_har_file_ with the respective path to the HAR file
- replace _output_csv_filename_ with the desired filename for the CSV results file, e.g. `harparser-results.csv`

Note, the output CSV file will be saved to the same folder that HarParser.py is located/being run from.
