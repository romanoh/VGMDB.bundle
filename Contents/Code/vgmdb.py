from logging import Logging

# Setup logger
log = Logging()


def search_albums(query):
    request = HTTP.Request(
        'http://vgmdb.info/search/albums?format=json&q=' + String.Quote(query)
    )
    try:
        request.load()
        result = JSON.ObjectFromString(request.content)
        log.info('VGMDB: Great it worked: ' + query)
        return result['results']['albums']
    except Exception as e:  # This is the correct syntax
        raise SystemExit(e)

    # log.error('VGMDB LINK: Error searching VGMDB - Album: ' + query)


def get_album(id):
    request = HTTP.Request(
        'http://vgmdb.info/album/' + id + '?format=json'
    )
    try:
        request.load()
        return JSON.ObjectFromString(request.content)
    except:
        log.error('Error getting album info')


def search_artists(query):
    request = HTTP.Request(
        'http://vgmdb.info/search/artists?format=json&q=' + String.Quote(query)
    )
    try:
        request.load()
        result = JSON.ObjectFromString(request.content)
        return result['results']['artists']
    except:
        log.error('Error searching VGMDB - Artist: ' + query)


def get_artist(id):
    request = HTTP.Request(
        'http://vgmdb.info/artist/' + id + '?format=json'
    )
    try:
        request.load()
        return JSON.ObjectFromString(request.content)
    except:
        log.error('Error getting artist info')
