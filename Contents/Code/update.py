from datetime import datetime
from vgmdb import get_album, get_artist
from logging import Logging

# Setup logger
log = Logging()


def get_lang(obj):
    if 'ja-latn' in obj:
        return obj['ja-latn']
    elif 'Romaji' in obj:
        return obj['Romaji']
    elif 'en' in obj:
        return obj['en']
    elif 'English' in obj:
        return obj['English']
    elif 'ja' in obj:
        return obj['ja']
    elif 'Japanese' in obj:
        return obj['Japanese']
    else:
        return None


def get_poster(metadata, thumb, full):
    try:
        thumbnail = Proxy.Preview(HTTP.Request(
            thumb, immediate=True
        ).content)
        metadata.posters[full] = thumbnail
    except:
        log.error('Error loading poster')


def update_album(metadata, media, force):
    result = get_album(metadata.id)

    metadata.genres = result['categories']

    metadata.collections = map(lambda p: get_lang(p['names']), result['products'])

    # metadata.rating = float(result['rating'])

    metadata.original_title = str(result['name'])
    if metadata.original_title is not None:
        log.info('UPDATE: Found original_title: %s', metadata.original_title)
    else:
        log.info('UPDATE: No original_title Found.')

    metadata.title = get_lang(result['names'])

    metadata.summary = result['notes']

    metadata.studio = get_lang(result['publisher']['names'])

    split = map(lambda s: int(s), result['release_date'].split('-'))
    release_date = datetime(split[0], split[1], split[2])
    metadata.originally_available_at = release_date

    get_poster(metadata, result['picture_small'], result['picture_full'])
    for poster in result['covers']:
        if poster['full'] != result['picture_full']:
            get_poster(metadata, poster['thumb'], poster['full'])

    trackNum = 0
    for disc in result['discs']:
        for track in disc['tracks']:
            trackNum = trackNum + 1

            metadata.tracks[trackNum].name = get_lang(track['names'])

    # Writes metadata information to log.
    log.separator(msg='New data', log_level="info")

    # Log basic metadata
    data_to_log = [
        {'ID': metadata.id},
        {'Title': metadata.title},
        {'Release date': str(metadata.originally_available_at)},
        {'Studio': metadata.studio},
        {'Summary': metadata.summary},
    ]
    log.metadata(data_to_log, log_level="info")

    # Log basic metadata stored in arrays
    multi_arr = [
        {'Genres': metadata.genres},
        {'Moods': metadata.moods},
        {'Styles': metadata.styles},
    ]
    log.metadata_arrs(multi_arr, log_level="info")

    log.separator(log_level="info")


def update_artist(metadata, media, force):
    result = get_artist(metadata.id)

    # metadata.rating = float(result['info']['Weighted album rating'].replace('/10', ''))
    metadata.title = result['name']
    metadata.summary = result['notes']
    # metadata.genres = str(result['type'])
    # metadata.country = result['birthplace']

    if result['picture_full'] is not None:
        get_poster(metadata, result['picture_small'], result['picture_full'])

