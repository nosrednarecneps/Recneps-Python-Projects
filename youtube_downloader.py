import pytube
import sys

def exit(call):
    if call == "exit":
        sys.exit()

def help(call):
    if call == "help":
        print("\nYouTube Downloader: How to use\n")
        print(" - You must type the directory in which you will download your files to")
        print("     - C:\\Users\\SYSTEM_NAME_LOCATED_HERE\\Downloads")
        print("     - Remember, incorrectly typing in the directory may result in an unexpected error")
        print(" - You must type the link for the YouTube video you want to download")
        print(" - To exit the program, type 'exit'")
        print(" - To find out how to use the program, type 'help'")
        print(" - URL downloader coming soon!\n")

help("help")

while True:
    directory = str(input("Please type your directory: "))
    exit(directory)
    help(directory)
    download_link = directory
    print("File Location: " + download_link)
    link = input("Please paste the URL of the video you want to download: ")
    exit(link)
    help(link)
    try:
        yt = pytube.YouTube(link)
        print("     Downloading...")
        yd = yt.streams.get_highest_resolution()
        yd.download(download_link)
        print("     Download Complete!")
        break
    except pytube.exceptions.RegexMatchError and KeyError and pytube.exceptions.PytubeError:
        print("Sorry, we had a problem.")
