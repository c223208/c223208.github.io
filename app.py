import feedparser


rss_url = "https://https://ideamarkets.info/wp-admin/edit.php?post_type=post&author=8/rss"  # サイトのRSSフィードURL
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    title = entry.title
    date = entry.published
    summary = entry.summary[:50]  # 冒頭の50文字を取得
    print(f"{title} ({date}) - {summary}...")