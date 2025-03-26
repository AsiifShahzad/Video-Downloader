import yt_dlp
import os

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            'outtmpl': os.path.join(os.path.expanduser("~"), 'Downloads', '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': True,  # Prevent accidentally downloading entire playlists
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"✅ Downloaded: {info['title']} to your Downloads folder.")

    except Exception as e:
        print(f"⚠️ Error downloading {url}: {e}")

if __name__ == '__main__':
    try:
        # Always update yt-dlp before running
        os.system("python -m pip install -U yt-dlp")

        number_of_videos = int(input("Enter the number of videos you want to download: "))
        urls = []

        for i in range(number_of_videos):
            url = input(f"Enter URL for video {i+1}: ").strip()
            if url:
                urls.append(url)
            else:
                print("⚠️ Empty URL skipped.")

        print("\n🔽 Starting downloads...\n")
        for url in urls:
            download_video(url)

        input("\n✅ All downloads completed! Press Enter to exit.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
