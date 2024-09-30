import yt_dlp


def download_video(url):
    try:
        ydl_opts = {
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
