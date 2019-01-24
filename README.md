Manage urls of Google Chrome tabs.
Only for Mac.

# Setup
I reccomend to use virtualenv.

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

# Usage
## Output urls

```sh
>> python chrome.py > urls.txt
>> wc urls.txt
10
>> head urls.txt
http:// ...
http:// ...
http:// ...
http:// ...
```

- It does not save the urls with the domains listed in `blacklist.txt`.
- It does not save the urls in secret window.
- It automatically removes the duplicated tabs.
- It normalize arXiv urls from pdf to abs.


## Scheduling with crontab
Register crontab to record the urls, for example, every 30 minutes.


```sh
0/30 * * * * /path/to/this/repository/record.sh
```

it'll records to /path/to/this/repository/result/[YEAR]/[MONTH]/[DAY]/YYYYMMDD_HH.txt.
