import requests

REPO_OWNER = 'LayerZero-Labs'
REPO_NAME = 'sybil-report'
TOKEN_FROM_GITHUB = ''
# https://github.com/settings/tokens

headers = {
    'Authorization': f'Bearer {TOKEN_FROM_GITHUB}',
    'Accept': 'application/vnd.github.v3+json'
}


def get_issues(wallet):
    url = f'https://api.github.com/search/issues?q={wallet}+repo:{REPO_OWNER}/{REPO_NAME}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        issues = data.get('items', [])
        if len(issues) >0:
            return issues
        else:
            return None
    else:
        return None
