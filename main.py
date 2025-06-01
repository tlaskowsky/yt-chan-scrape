from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        video_id = input_data.get('videoId')

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            text_only = " ".join([entry['text'] for entry in transcript])
            await Actor.push_data({'videoId': video_id, 'transcript': text_only})
        except (TranscriptsDisabled, NoTranscriptFound):
            await Actor.push_data({'videoId': video_id, 'transcript': None, 'error': 'Transcript not available'})
        except Exception as e:
            await Actor.push_data({'error': str(e)})
