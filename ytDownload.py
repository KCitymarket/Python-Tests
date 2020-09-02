from pytube import YouTube

# this really sucks tbh. it's not just my code but pytube library sucks too.
# if this doesnt work download pytube3 with "pip install pytube3"
# if it still doesnt work its most likely because of KeyError: 'cipher'
# if you get that error go to "extract.py" and around line 300 you have to correct 
# parse_qs(formats[i]["Cipher"]) to parse_qs(formats[i]["signatureCipher"])

def crap():
    print("Youtube video url:")
    url = input()

    print("Where do you want to download it? (full path)")
    path = input()

    print("video or a videoless video that you can rename to .mp3 to get audio?")
    qual = input("input video/audio ")
    

    if qual == "video":
        YouTube(url).streams.get_highest_resolution().download(path)
    elif qual == "audio":
        YouTube(url).streams.filter(only_audio=True).first().download(path)
    else:
        crap()
    
crap()

