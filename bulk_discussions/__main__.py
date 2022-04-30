from pyflarum import FlarumUser
from pyflarum.client.flarum.core.discussions import PreparedDiscussion

import time

from pathlib import Path
from argparse import ArgumentParser



def main():
    parser = ArgumentParser()
    parser.add_argument('--forum_url', '--url', '-f', help='Forum URL to create discussions for.', required=True)
    parser.add_argument('--username', '-u', help='Username to log into.', required=True)
    parser.add_argument('--password', '-p', help='Password for the user.', required=True)
    args = parser.parse_args()

    try:
        USER = FlarumUser(forum_url=args.forum_url, username_or_email=args.username, password=args.password)
    
    except Exception as error:
        return print(f"An error occured. Are your credentials correct? ({error})")


    for file in Path(Path(__file__).parent.parent / 'discussions').iterdir():
        created = PreparedDiscussion(user=USER, title=file.stem, content=file.read_text(encoding='UTF-8')).create()
        print(f'Created discussion "{created.title}" with ID `{created.id}`: {created.url}')
        # time.sleep(...) # Uncomment to sleep for X seconds to avoid rate limiting.



if __name__ == '__main__':
    main()
