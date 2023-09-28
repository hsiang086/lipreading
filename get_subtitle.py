from youtube_transcript_api import YouTubeTranscriptApi

def get_subtitle(video_id):
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW'])
    with open(f"./data/subtitles/subtitles.py", "a") as f:
        f.write(f"\n{video_id} = [\n")
        for line in srt:
            f.write(f"\t{line},\n")
        f.write("]")
    return srt

get_subtitle("znJbiTVg6_M")