import argparse
import datetime
import os

from chrome_app import Chrome


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--blacklist', type=str, default='blacklist.txt')
    parser.add_argument('--save_dir', type=str, default='result')
    args = parser.parse_args()

    chrome = Chrome(args.blacklist)
    ret = chrome.get_all_urls(delete_duplications=True)
    urls = ret['urls']
    duplicated = ret['duplicated']

    if len(urls) == 1 and urls[0] == 'chrome://newtab/':
        urls = []

    now = datetime.datetime.now()
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            args.save_dir)
    save_dir = os.path.join(
        base_dir, str(now.year), '{:02d}'.format(now.month), str(now.day))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)
    nowstr = now.strftime('%Y%m%d_%H%M')
    save_path = os.path.join(save_dir, '{}.txt'.format(nowstr))
    log_path = os.path.join(base_dir, 'log.txt')

    with open(save_path, 'w') as f:
        f.write('\n'.join(urls) + '\n')

    with open(log_path, 'a') as f:
        f.write('{}\t{}\t{}\n'.format(nowstr, len(urls), len(duplicated)))
