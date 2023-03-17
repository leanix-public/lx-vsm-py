# LX-VSM-PY

## What is it? 

This is a python based CLI to submit project information, including a [CycloneDX](https://cyclonedx.org/) compliant SBOM, to your [LeanIX VSM](https://www.leanix.net/en/products/value-stream-management) workspace via the [Service Discovery API](https://docs-vsm.leanix.net/reference/discovery_service).

## When should I use it?

Primarily used for submitting an SBOM during your CI/CD pipeline, but can be used to submit additional data during various stages of development and deployment, such as version numbers, testing results, code quality, and deployment times.

## How does it work?

Assuming your python packages are on your system `$PATH` variable, this can be run like any other bash tool just by calling `lx-vsm-py`. Arguments can be seen by running `lx-vsm-py --help`. This script uses the arguments to authenticate with your workspace to submit the other arguments and (optional) SBOM to the [Service Discovery API](https://docs-vsm.leanix.net/reference/discovery_service). See the next section for detailed instructions.

## How do I use it?

1. Clone this repository to your computer
2. Run `python setup.py sdist && pip install dist/lx-vsm-py-1.0.tar.gz` to build and install this utility to your local python installation globally.
3. Add a file to your python project called `lx-vsm-py.sh` with the following contents:
```sh
cyclonedx-py -e -F --format json -o sbom.json &&  lx-vsm-py --file sbom.json --api_token $VSM_TOKEN --region us --host demo-us
```
4. Update the region, host, and api-token for your instance of VSM
5. Run `./lx-vsm-py.sh` to update your service in VSM

## License

This project is licensed under the MIT License

## Contact

Start with the [VSM Documentation](https://docs-vsm.leanix.net/docs), or feel free to contact [LeanIX Support](https://leanix.zendesk.com/hc/en-us/community/topics) for anything else.
