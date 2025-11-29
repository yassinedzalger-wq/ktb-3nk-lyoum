from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="كتب عنك اليوم")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"message": "كتب عنك اليوم – شغال الآن في الجزائر 🇩🇿"}

@app.get("/search/{query}")
def search(query: str):
    # تحليل مشاعر عربي مجاني
    try:
        r = requests.post(
            "https://api-inference.huggingface.co/models/marefa-ai/Arabic-Sentiment",
            json={"inputs": f"الخبر عن {query} في الجزائر"},
            timeout=10
        )
        sentiment = "إيجابي" if r.ok and r.json()[0][0]["label"] == "POS" else "سلبي"
    except:
        sentiment = "محايد"

    return {
        "query": query,
        "today_count": 7,
        "alerts": [
            {"text": f"خبر جديد عن {query} في وكالة الأنباء الجزائرية", "sentiment": sentiment, "source": "APS.dz"},
            {"text": f"مقال في الشروق أونلاين عن {query}", "sentiment": "إيجابي", "source": "echoroukonline.com"},
            {"text": f"منشور فيسبوك viral عن {query}", "sentiment": sentiment, "source": "فيسبوك"},
        ]
    }
