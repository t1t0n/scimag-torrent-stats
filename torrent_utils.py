import hashlib

import bencodepy
import requests
from bs4 import BeautifulSoup

from scraper import scrape


def get_torrent_stats(url):
    response = requests.get(url)
    data = bencodepy.decode(response.content)

    info_hash = hashlib.sha1(bencodepy.bencode(data[b"info"])).hexdigest()

    trackers_list = data[b'announce-list']

    stats = {'seeds':0, 'peers':0}

    for tracker_url in trackers_list:
        tracker_url = tracker_url[0].decode('utf-8')
        result = scrape(tracker_url, [info_hash])
        if not result:
            continue

        stats['seeds'] = max(stats['seeds'], result[info_hash]['seeds'])
        stats['peers'] = max(stats['peers'], result[info_hash]['peers'])
    return stats


def get_scimag_torrents():
    page = requests.get("http://libgen.rs/scimag/repository_torrent/")
    soup = BeautifulSoup(page.content, 'html.parser')
    url_elements = soup.find_all(lambda tag:tag.name=="a" and ".torrent" in tag['href'])
    urls = []
    for url_element in url_elements:
        torrent_filename = url_element['href']
        torrent_url = f"http://libgen.rs/scimag/repository_torrent/{torrent_filename}"
        urls.append(torrent_url)
    return urls
