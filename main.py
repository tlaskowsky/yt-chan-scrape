from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        video_id = input_data.get('videoId')

        print(f"📥 Received input: videoId = {video_id}")

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            print(f"✅ Transcript fetched. {len(transcript)} segments")
            text_only = " ".join([entry['text'] for entry in transcript])
            await Actor.push_data({'videoId': video_id, 'transcript': text_only})
            print("📤 Transcript pushed to dataset.")
        except (TranscriptsDisabled, NoTranscriptFound):
            await Actor.push_data({'videoId': video_id, 'transcript': None, 'error': 'Transcript not available'})
            print("⚠️ Transcript not available.")
        except Exception as e:
            await Actor.push_data({'videoId': video_id, 'error': str(e)})
            print(f"❌ Error: {str(e)}")

        await Actor.exit()


import asyncio
asyncio.run(main())
