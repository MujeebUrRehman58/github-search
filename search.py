import os
import sys
from math import ceil

from github import Github
from prettytable import PrettyTable

APP_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(APP_PATH)

ACCESS_TOKEN = os.environ['GE_ACCESS_TOKEN']
HOSTNAME = os.environ.get('GE_HOSTNAME')
SEARCH_KEYWORD = 'export'

if HOSTNAME:
    g = Github(base_url=f"https://{HOSTNAME}/api/v3", login_or_token=f"{ACCESS_TOKEN}")
else:
    g = Github(ACCESS_TOKEN)


def search_github():
    query = f'{SEARCH_KEYWORD} in:file'
    result = g.search_code(query)
    page = 0
    page_size = 20

    print(f'Found {result.totalCount} file(s)')
    print(f'Displaying files with page size of {page_size}')
    try:
        for i in range(ceil(len(range(result.totalCount)) / page_size)):
            t = PrettyTable(['File name', 'Status', 'File URL'])
            for file in result[page * page_size:(page + 1) * page_size]:
                t.add_row([file.name, 'Private' if file.repository.private else 'Public', file.html_url])
            page += 1
            print(t)
            next_page = input('Display Next page? Enter "Y/N": ')
            if next_page.lower() == 'n':
                break
    except:
        pass


if __name__ == '__main__':
    search_github()