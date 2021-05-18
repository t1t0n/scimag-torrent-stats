from db_utils import upsert_torrent_stats
from torrent_utils import get_scimag_torrents, get_torrent_stats

print('Started scraper')
while True:
    urls = get_scimag_torrents()

    for url in urls:
        print(f"Processing URL: {url}")
        stats = get_torrent_stats(url)
        upsert_torrent_stats(url, stats)