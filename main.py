import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

# Global parameters
vol = 70
end_vol = 20
vol_iterations = 4
T  = 15*60
client_id = "c7eac290d7054303b0455309eff628c2" # SPOTIPY_CLIENT_ID 
client_secret = "a0e85f57c39e4d2aa74dcc3724ec3db1" # SPOTIPY_CLIENT_SECRET 
redirect_uri = "https://localhost:8888/callback/" # SPOTIPY_REDIRECT_URI

'''
Windows:
    set SPOTIPY_CLIENT_ID=c7eac290d7054303b0455309eff628c2
    set SPOTIPY_CLIENT_SECRET=a0e85f57c39e4d2aa74dcc3724ec3db1
    set SPOTIPY_REDIRECT_URI=https://localhost:8888/callback/

'''
if __name__ == "__main__":
    
    scope = ["user-read-playback-state", "user-modify-playback-state", "user-read-currently-playing"]
    auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, show_dialog=True, scope=scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    print(f"auth: {auth_manager}")

    playlists = sp.user_playlists('5bmlfppuglfo7564jt0dsp43m')
    freddan_list = None
    for i in range(len(playlists['items'])):
        if playlists['items'][i]['name'] == 'Freddan':
            freddan_list = playlists['items'][i]
            break
    if freddan_list is None:
        print("Error! Could not find \'freddan\' playlist :((")
        print("Now exiting...")
        exit()
    
    device_id="b028202bf3183ab5f0804c55a02d2d5f19ce3ede"
    # Set volume to 70
    sp.volume(vol, device_id)

    # Start playback
    sp.start_playback(device_id="b028202bf3183ab5f0804c55a02d2d5f19ce3ede",
                      context_uri=freddan_list['uri'],
                      uris=None, offset=None, position_ms=None)


    # Adjust volume slowly
    vol_step = (vol - end_vol)/vol_iterations
    for i in range(vol_iterations):
        time.sleep(20)
        vol -= vol_step
        sp.volume(int(vol), device_id)

    # Playing loop
    start_time = time.time()
    while(time.time() - start_time < T):
        time.sleep(5)
    
    sp.pause_playback(device_id)
    
