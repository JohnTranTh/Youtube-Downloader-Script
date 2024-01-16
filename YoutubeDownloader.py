from pytube import YouTube

def download_video(url, output_directory, audio_only):
    try:
        video = YouTube(url)

        if audio_only:
            audio_stream = video.streams.filter(only_audio=True).first()
            print_file_info(video)
            print(str(audio_stream.filesize_mb) + "MBs")
            audio_stream.download(output_path = output_directory)
            print("Download Successful")
        else:
            video_stream = video.streams.get_highest_resolution()
            print_file_info(video)
            print(str(video_stream.filesize_mb) + "MBs")
            video_stream.download(output_path = output_directory)
            print("Download Successful")
    except:
        print("Download Failed")

def print_file_info(video):
    print("Video Information:")
    print("Title: " + video.title)
    print("Author: " + video.author)
    print("Length: " + str(video.length))

if __name__ == "__main__":
    video_url = input("Enter a Youtube URL: ")
    audio_only = input("Do you want only audio (enter y if yes): ").lower()

    if audio_only == 'y':
        audio_only = True
    else:
        audio_only = False

    output_location = input("Enter the location where you wish for the file to be saved (leave blank for current directory): ").strip()

    if output_location == ' ':
        output_location = '.'

    download_video(video_url, output_location, audio_only)
