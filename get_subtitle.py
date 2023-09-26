from youtube_transcript_api import YouTubeTranscriptApi

def get_subtitle(video_id):
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW'])
    with open("subtitle.txt", "w") as f:
        for line in srt:
            f.write(f"{line}\n")
    return srt

get_subtitle("znJbiTVg6_M")