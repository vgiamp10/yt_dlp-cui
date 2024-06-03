import yt_dlp

print("""
        BENVENUTO IN YOUTUBE DOWNLOADER By vgiamp10
        COSA VUOI SCARICARE?
        1. Video
        2. Playlist (video)
        3. Playlist (audio) (richiede ffmpeg)
        4. Audio (richiede ffmpeg)""")
scelta = input("Scelta: ")
if scelta == "1":
    url = input("Inserisci l'URL del video: ")
    ydl_opts = {'extract_flat': 'discard_in_playlist',  # Inizio segmento di codice per la rimozione degli sponsor
                'fragment_retries': 10,
                'ignoreerrors': 'only_download',
                'postprocessors': [{'api': 'https://sponsor.ajay.app',
                                    'categories': {'filler',
                                                   'interaction',
                                                   'intro',
                                                   'music_offtopic',
                                                   'outro',
                                                   'preview',
                                                   'selfpromo',
                                                   'sponsor'},
                                    'key': 'SponsorBlock',
                                    'when': 'after_filter'},
                                   {'force_keyframes': False,
                                    'key': 'ModifyChapters',
                                    'remove_chapters_patterns': [],
                                    'remove_ranges': [],
                                    'remove_sponsor_segments': {'filler',
                                                                'interaction',
                                                                'intro',
                                                                'music_offtopic',
                                                                'outro',
                                                                'preview',
                                                                'selfpromo',
                                                                'sponsor'},
                                    'sponsorblock_chapter_title': '[SponsorBlock]: '
                                                                  '%(category_names)l'},
                                   {'key': 'FFmpegConcat',
                                    'only_multi_video': True,
                                    'when': 'playlist'}],
                'retries': 10,  # Fine segmento di codice per la rimozione degli sponsor
                'format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
elif scelta == "2":
    url = input("Inserisci l'URL della playlist: ")
    ydl_opts = {'extract_flat': 'discard_in_playlist',  # Inizio segmento di codice per la rimozione degli sponsor
                'fragment_retries': 10,
                'ignoreerrors': 'only_download',
                'postprocessors': [{'api': 'https://sponsor.ajay.app',
                                    'categories': {'filler',
                                                   'interaction',
                                                   'intro',
                                                   'music_offtopic',
                                                   'outro',
                                                   'preview',
                                                   'selfpromo',
                                                   'sponsor'},
                                    'key': 'SponsorBlock',
                                    'when': 'after_filter'},
                                   {'force_keyframes': False,
                                    'key': 'ModifyChapters',
                                    'remove_chapters_patterns': [],
                                    'remove_ranges': [],
                                    'remove_sponsor_segments': {'filler',
                                                                'interaction',
                                                                'intro',
                                                                'music_offtopic',
                                                                'outro',
                                                                'preview',
                                                                'selfpromo',
                                                                'sponsor'},
                                    'sponsorblock_chapter_title': '[SponsorBlock]: '
                                                                  '%(category_names)l'},
                                   {'key': 'FFmpegConcat',
                                    'only_multi_video': True,
                                    'when': 'playlist'}],
                'retries': 10,  # Fine segmento di codice per la rimozione degli sponsor
                'format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
                'yesplaylist': True,
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
elif scelta == "3":
    url: str = input("Inserisci l'URL della playlist: ")
    ydl_opts = {'extract_flat': 'discard_in_playlist',
 'final_ext': 'mp3',
 'format': 'bestaudio/best',
 'fragment_retries': 10,
 'ignoreerrors': True,
 'outtmpl': {'default': '%(title)s.%(ext)s'},
 'postprocessors': [{'api': 'https://sponsor.ajay.app',
                     'categories': {'filler',
                                    'interaction',
                                    'intro',
                                    'music_offtopic',
                                    'outro',
                                    'preview',
                                    'selfpromo',
                                    'sponsor'},
                     'key': 'SponsorBlock',
                     'when': 'after_filter'},
                    {'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'mp3',
                     'preferredquality': '0'},
                    {'force_keyframes': False,
                     'key': 'ModifyChapters',
                     'remove_chapters_patterns': [],
                     'remove_ranges': [],
                     'remove_sponsor_segments': {'filler',
                                                 'interaction',
                                                 'intro',
                                                 'music_offtopic',
                                                 'outro',
                                                 'preview',
                                                 'selfpromo',
                                                 'sponsor'},
                     'sponsorblock_chapter_title': '[SponsorBlock]: '
                                                   '%(category_names)l'},
                    {'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
 'retries': 10}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

elif scelta == "4":
    url = input("Inserisci l'URL del video: ")
    ydl_opts = {'extract_flat': 'discard_in_playlist',
 'final_ext': 'mp3',
 'format': 'bestaudio/best',
 'fragment_retries': 10,
 'ignoreerrors': True,
 'noplaylist': True,
 'outtmpl': {'default': '%(title)s.%(ext)s'},
 'postprocessors': [{'api': 'https://sponsor.ajay.app',
                     'categories': {'filler',
                                    'interaction',
                                    'intro',
                                    'music_offtopic',
                                    'outro',
                                    'preview',
                                    'selfpromo',
                                    'sponsor'},
                     'key': 'SponsorBlock',
                     'when': 'after_filter'},
                    {'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'mp3',
                     'preferredquality': '0'},
                    {'force_keyframes': False,
                     'key': 'ModifyChapters',
                     'remove_chapters_patterns': [],
                     'remove_ranges': [],
                     'remove_sponsor_segments': {'filler',
                                                 'interaction',
                                                 'intro',
                                                 'music_offtopic',
                                                 'outro',
                                                 'preview',
                                                 'selfpromo',
                                                 'sponsor'},
                     'sponsorblock_chapter_title': '[SponsorBlock]: '
                                                   '%(category_names)l'},
                    {'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
 'retries': 10}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
