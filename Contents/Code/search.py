import vgmdb
# Import internal tools
from logging import Logging

# Setup logger
log = Logging()

def search_albums(results, media, lang):

    query = media.album

    if query is None:
        query = media.filename
		
    result = vgmdb.search_albums(query)

    if result is None:
        return
	
    s = 100
    for album in result:
        results.Append(MetadataSearchResult(
            id = album['link'].replace('album/', ''),
            name = album['titles']['en'],
            year = album['release_date'][0:4],
            score = s,
            lang = lang
        ))
        s = s - 1
		
	# Write search result status to log
	if not result:
		log.warn('SEARCH: No results found for query.')
	else:
		log.debug('SEARCH: Found %s result(s) for query',len(result))
		log.debug('SEARCH: %s',result)

def search_artists(results, media, lang):

    query = media.artist
	
    if query is None:
        query = media.name
		
		
    result = vgmdb.search_artists(query)

    if result is None:
        return

    s = 100
    for artist in result:
        results.Append(MetadataSearchResult(
            id = artist['link'].replace('artist/', ''),
            name = artist['names']['en'],
            score = s,
            lang = lang
        ))
        s = s - 1