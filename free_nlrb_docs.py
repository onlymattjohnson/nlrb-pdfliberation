import feedparser

board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')
board_decisions_entries = board_decisions_feed['entries']

print board_decisions_entries[0]['links'][0]['href']
