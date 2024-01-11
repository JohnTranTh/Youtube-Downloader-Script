from pytube import YouTube

def download_video(url, audio_only):
    video = YouTube(url)

    if audio_only:
        audio_stream = video.streams.filter(only_audio=True).first()
        print_file_info(video)
        audio_stream.download()
    else:
        video_stream = video.streams.get_highest_resolution()
        print_file_info(video)
        video_stream.download()

def print_file_info(video):
    filesize = video.streams.get_highest_resolution().filesize_mb
    
    print("Title: " + video.title)
    print("Length: " + str(video.length))
    print(str(filesize) + "MBs")

if __name__ == "__main__":
    video_url = input("Enter a Youtube URL")
    audio_only = input("Do you want only audio (enter y if yes): ").lower()
    if audio_only == 'y':
        audio_only = True
    else:
        audio_only = False
    download_video(video_url, audio_only)
    print("File Downloaded")
