from gitrepo.get_reports import get_issues
import re


def find_issues_by_wallets(wallets):
    for wallet in wallets:
        issues = get_issues(wallet)
        if issues is not None:
            print(f'{wallet} | Найдено {len(issues)} issues:')
            for issue in issues:
                print(f"- #{issue['number']} {issue['title']}")

                description_match = re.search(r'# Description\s+(.+)', issue['body'])
                methodology_match = re.search(r'# Detailed Methodology & Walkthrough\s+(.+)', issue['body'])

                if description_match:
                    description = description_match.group(1).strip()
                    print(f'Description: {description}')

                if methodology_match:
                    methodology = methodology_match.group(1).strip()
                    print(f'Methodology: {methodology}')

            print(f'__________________________________________')


def main():
    with open("wallets.txt", "r") as file:
        wallets = file.read().splitlines()
    find_issues_by_wallets(wallets)
    print('Скрипт отработал')


if __name__ == "__main__":
    main()
