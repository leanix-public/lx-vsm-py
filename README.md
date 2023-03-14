# LX-VSM-PY

## How to use this package

1. Clone this repository to your computer
2. Run `python setup.py sdist && pip install dist/lx-vsm-py-1.0.tar.gz` to build and install this utility to your local python installation globally.
3. Add a file to your python project called `lx-vsm-py.sh` with the following contents:
```sh
cyclonedx-py -e -F --format json -o sbom.json &&  lx-vsm-py --file sbom.json --api_token $VSM_TOKEN --region us --host demo-us
```
4. Update the region, host, and api-token for your instance of VSM
5. Run `./lx-vsm-py.sh` to update your service in VSM