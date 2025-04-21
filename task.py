import yt_dlp
import os

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[height>=720]+bestaudio/best',  # Get at least 720p quality
            'outtmpl': os.path.join(os.path.expanduser("~"), 'Downloads', '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Ensures MP4 output
            'noplaylist': True,  # Prevents downloading playlists
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',  # Converts final video to MP4
                    'preferedformat': 'mp4'  # <-- Fix: Correct argument spelling
                }
            ]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Downloaded: {info['title']} to your Downloads folder.")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == '__main__':
    try:
        # Always update yt-dlp before running
        print("Updating yt-dlp...")
        os.system("python -m pip install -U yt-dlp")

        number_of_videos = int(input("Enter the number of videos you want to download: "))
        urls = []

        for i in range(number_of_videos):
            url = input(f"Enter URL for video {i+1}: ").strip()
            if url:
                urls.append(url)
            else:
                print("Empty URL skipped.")

        print("\nStarting downloads...\n")
        for url in urls:
            download_video(url)

        input("\n✅ All downloads completed! Press Enter to exit.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

