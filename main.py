from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('videoId')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text_only = " ".join([entry['text'] for entry in transcript])
        return jsonify({'videoId': video_id, 'transcript': text_only})
    except (TranscriptsDisabled, NoTranscriptFound):
        return jsonify({'videoId': video_id, 'transcript': None, 'error': 'Transcript not available'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
