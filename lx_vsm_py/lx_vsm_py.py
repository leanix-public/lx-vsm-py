import argparse
import requests

def get_access_token(api_token, host):
    """
    Get an access token using the provided API token and host.
    """
    url = f"https://{host}.leanix.net/services/mtm/v1/oauth2/token"
    data = {
        "grant_type": "client_credentials",
    }
    response = requests.post(
        url,
        auth=requests.auth.HTTPBasicAuth("apitoken", api_token),
        data=data,
    )
    if response.status_code != 200:
        raise ValueError("Failed to get access token.")
    return response.json()["access_token"]


def upload_file(file_path, region, access_token):
    """
    Upload the given file to the LeanIX VSM Service Discovery API.
    """
    url = f"https://{region}-vsm.leanix.net/services/vsm/discovery/v1/service"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "id": "test_id",
        "sourceType": "python3",
        "sourceInstance": "lx-vsm-python",
        "name": "test_name",
        "description": "test_description",
    }
    with open(file_path, "rb") as f:
        files = {"bom": f}
        response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code != 200:
        raise ValueError("Failed to upload file.")
    
def main():
  parser = argparse.ArgumentParser(description='Upload CycloneDX files to LeanIX VSM Service Discovery API')

  parser.add_argument('--file', help='The path to the CycloneDX file to upload')
  parser.add_argument('--api_token', help='The API token to use for authentication')
  parser.add_argument('--region', help='The region to use for uploading the file (e.g., "us" or "eu")')
  parser.add_argument('--host', help='The host to use for authenticating (e.g., acme.leanix.net would be "acme")')
  args = parser.parse_args()

  access_token = get_access_token(args.api_token, args.host)
  if access_token:
      upload_file(args.file, args.region, access_token)
      print("Complete!")
