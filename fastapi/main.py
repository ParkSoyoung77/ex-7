from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/api", response_class=HTMLResponse)
async def get_fastapi_page():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>FastAPI Backend Page</title>
        <style>
            body { 
                font-family: 'Segoe UI', sans-serif; 
                text-align: center; padding: 50px; 
                background: linear-gradient(135deg, #232f3e 0%, #37475a 100%); /* AWS 다크 블루 테마 */
                margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center;
            }
            .card { 
                background: white; padding: 40px; border-radius: 15px; 
                box-shadow: 0 10px 25px rgba(0,0,0,0.4); max-width: 500px;
            }
            h1 { color: #232f3e; }
            .api-badge {
                display: inline-block; background-color: #0073bb; color: white;
                padding: 5px 15px; border-radius: 20px; font-size: 0.9em; margin-top: 15px;
            }
            .info { color: #666; font-size: 0.9em; margin-top: 20px; text-align: left; background: #f9f9f9; padding: 15px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>⚡ FastAPI Backend Node</h1>
            <p>이 페이지는 <strong>FastAPI 컨테이너</strong>에서<br>직접 생성하여 반환된 HTML입니다.</p>
            <div class="api-badge">Endpoint: /api</div>
            
            <div class="info">
                <strong>🖥️ Server Info:</strong><br>
                • Domain: aaa.sy99.cloud<br>
                • Service: Python FastAPI<br>
                • Infra: AWS ALB & EC2
            </div>
            
            <hr style="margin: 20px 0; border: 0; border-top: 1px solid #eee;">
            <p style="font-size: 0.8em; color: #888;">Nginx를 거쳐 FastAPI 노드에 도달했습니다.</p>
            <a href="/" style="text-decoration: none; color: #0073bb; font-size: 0.8em;">메인 페이지(Nginx)로 돌아가기</a>
        </div>
    </body>
    </html>
    """

# ALB Health Check용
@app.get("/health")
def health():
    return {"status": "ok"}