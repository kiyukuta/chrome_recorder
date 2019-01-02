import argparse
import re
import sys

import appscript


class Chrome(object):

    def __init__(self, blacklist_path='blacklist.txt'):
        self.app = appscript.app("Google Chrome")

        self.blacklist = []  # domains
        if blacklist_path:
            with open(blacklist_path) as f:
                self.blacklist = [l.strip() for l in f]

        self.arxiv_reg = re.compile(
            r'https://arxiv.org/(?P<mode>(pdf|abs))/(?P<id>[0-9\.v]+)(.pdf)?')

    def in_blacklist(self, url):
        if not self.blacklist:
            return False
        return any([b in url for b in self.blacklist])

    def get_all_windows(self):
        windows = self.app.windows()
        # w.mode() == incognito: secret window
        return [w for w in windows if w.mode() == 'normal']

    def get_all_tabs(self, windows=None):
        assert type(windows) in [type(None), list]
        #if type(windows) == list:
        #    hoge = ???
        #    assert all(type(w) == hoge for w in windows)

        windows = windows or self.get_all_windows()
        for window in windows:
            for tab in window.tabs.get():
                yield tab

    def get_all_urls(self, delete_duplications=False):
        duplicated = []

        urls = set([])
        for tab in self.get_all_tabs():
            url = tab.get().URL.get()
            if url == 'chrome://newtab/':
                continue

            if self.in_blacklist(url):
                continue

            # arXiv pdf2abs
            if url.startswith('http://arxiv.org/pdf')
                url = url.rstrip('.pdf').replace('pdf', 'abs')
                tab.URL.set(url)

            if url in urls:
                duplicated.append(url)
                if delete_duplications:
                    tab.delete()
                continue

            if url is not None:
                urls.add(url)


        return {'urls': urls,
                'n_windows': len(self.get_all_windows()),
                'duplicated': duplicated}


if __name__ == '__main__':
    chrome = Chrome()
    ret = chrome.get_all_urls(delete_duplications=True)
    urls = ret['urls']
    n_windows = ret['n_windows']
    print(n_windows)
    print('\n'.join(sorted(urls)))

