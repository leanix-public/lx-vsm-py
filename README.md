# lx-vsm-py

## Building 

`python setup.py sdist`

## Installing

`pip install dist/lx-vsm-py-1.0.tar.gz`

## Running

`cyclonedx-py -e -F --format json -o sbom.json &&  python -m lx_vsm_py sbom.json $VSM_TOKEN us demo-us`
or
`cyclonedx-py -e -F --format json -o sbom.json &&  lx-vsm-py --file sbom.json --api_token $VSM_TOKEN --region us --host demo-us`
