import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math

def main(): 
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,
                                               client_secret=SECRET,
                                               redirect_uri=URI,
                                               scope="user-read-recently-played"))

    recentPlayed = sp.current_user_recently_played()
    for x in recentPlayed['items'][0]['track']:
        print(x)

    track = recentPlayed['items'][0]['track']

    duration = str(math.floor((track['duration_ms']/1000) / 60)) + "." + str(math.floor((track['duration_ms']/1000) % 60))
    print(duration)
    trackInfo = [track['name'], track['album']['name'], duration]
    
    print(trackInfo)


main()
