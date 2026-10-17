import os
import time
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Completely English interface for your future global clients
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Video Studio - Create Cinematic Videos</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #121212; color: white; text-align: center; padding-top: 80px; }
        .container { max-width: 600px; margin: 0 auto; background: #1e1e1e; padding: 40px; border-radius: 16px; box-shadow: 0 4px 30px rgba(0,0,0,0.5); }
        h1 { color: #007BFF; margin-bottom: 10px; }
        input { width: 90%; padding: 15px; font-size: 16px; border-radius: 8px; border: 1px solid #333; background: #2a2a2a; color: white; margin-bottom: 20px; }
        button { width: 95%; padding: 15px; font-size: 16px; background: #007BFF; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; }
        button:hover { background: #0056b3; }
        .result { margin-top: 30px; }
        video { max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,123,255,0.3); }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Video Studio</h1>
        <p style="color: #aaa; margin-bottom: 30px;">Generate professional AI videos for just $20/month</p>

        <form action="/generate" method="POST">
            <input type="text" name="prompt" placeholder="Example: astronaut cat walking on Mars..." required>
            <br>
            <button type="submit">Generate Video with ChatGPT & AI</button>
        </form>

        {% if video_url %}
        <div class="result">
            <h3 style="color: #28a745;">Video successfully generated for: "{{ user_prompt }}"</h3>
            <video src="{{ video_url }}" controls autoplay loop preload="auto" style="background: #000;"></video>
        </div>
        {% endif %}
    </div>
</body>
</html>"""


@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/generate', methods=['POST'])
def generate():
    user_idea = request.form.get('prompt')

    print(f"Received request for idea: {user_idea}")

    # Simulating 2 seconds of AI processing
    time.sleep(2)

    # Reliable video sample link
    test_video_url = "https://w3schools.com"

    return render_template_string(HTML_TEMPLATE, video_url=test_video_url, user_prompt=user_idea)


if __name__ == '__main__':
    # 0.0.0.0 is required for hosting platforms to allow external connections
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)