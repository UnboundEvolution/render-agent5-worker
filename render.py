from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import datetime

app = FastAPI()

@app.post("/render-job")
async def render_job(request: Request):
    data = await request.json()

    script_id = data.get("script_id", "unknown")
    total_scenes = data.get("total_scenes", 0)
    timeline = data.get("timeline", [])
    voiceover_url = data.get("voiceover_url", "null")

    print(f"🎬 Render request received for script: {script_id}")
    print(f"Scenes: {total_scenes}, Timeline length: {len(timeline)}, Voiceover: {voiceover_url}")

    render_output_url = f"https://cdn.example.com/videos/{script_id}.mp4"

    return JSONResponse(
        status_code=200,
        content={
            "script_id": script_id,
            "status": "done",
            "render_url": render_output_url,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
    )

if __name__ == "__main__":
   import os
port = int(os.environ.get("PORT", 8000))
uvicorn.run(app, host="0.0.0.0", port=port)
