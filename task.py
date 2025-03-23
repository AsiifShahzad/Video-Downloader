import yt_dlp
import os

def download_video(url):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(os.path.expanduser("~"), 'Downloads', '%(title)s.%(ext)s'),
            'format': 'best[height=480]+bestaudio/best[height=480]/best',
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"✅ Downloaded: {info['title']} to your Downloads folder.")
    except Exception as e:
        print(f"⚠️ Error occurred with {url}: {e}")

if __name__ == '__main__':
    try:
        number_of_videos = int(input("Enter the number of videos you want to download: "))
        urls = []

        for i in range(number_of_videos):
            url = input(f"Enter URL for video {i+1}: ").strip()
            urls.append(url)

        print("\n🔽 Starting downloads...\n")
        for url in urls:
            download_video(url)

        input("\n✅ All downloads completed! Press Enter to exit.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
