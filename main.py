import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI(title="Seismic Quiz Bot API")
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# 10-ti Seismic Network Quiz er Database
SEISMIC_QUIZZES = [
    {
        "id": 1,
        "question": "What is the primary focus of Seismic Systems?",
        "options": ["A) Public gaming networks", "B) Privacy-preserving, compliance-friendly blockchain for fintech", "C) Decentralized storage for video streaming", "D) High-frequency NFT trading platforms"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "Which institutions are primarily targeted by Seismic's privacy infrastructure?",
        "options": ["A) Traditional art museums", "B) Neobanks and institutional fintechs", "C) Decentralized autonomous organizations (DAOs) only", "D) Social media influencers"],
        "correct_answer": "B"
    },
    {
        "id": 3,
        "question": "How does Seismic approach financial regulation and compliance?",
        "options": ["A) By completely ignoring global regulations", "B) By building compliance-friendly mechanisms into the privacy network", "C) By avoiding on-chain transactions entirely", "D) By operating only in unregulated regions"],
        "correct_answer": "B"
    },
    {
        "id": 4,
        "question": "What core feature does Seismic offer to neobanks for secure on-chain operations?",
        "options": ["A) Zero privacy shields", "B) Protocol-level encryption with compliance capability", "C) Publicly visible wallet transaction balances", "D) Centralized database tracking"],
        "correct_answer": "B"
    },
    {
        "id": 5,
        "question": "Seismic ensures privacy-preserving transactions. What does 'privacy-preserving' mean in this context?",
        "options": ["A) Transactions are completely anonymous to everyone, including regulators", "B) Sensitive financial data remains confidential while maintaining compliance visibility", "C) All smart contracts are open for public data scraping", "D) Funds are locked forever in a black box"],
        "correct_answer": "B"
    },
    {
        "id": 6,
        "question": "Which layer of the tech stack does Seismic implement its encryption mechanisms?",
        "options": ["A) Only on the frontend UI", "B) At the protocol-level infrastructure", "C) Inside third-party browser extensions", "D) Through standard centralized APIs"],
        "correct_answer": "B"
    },
    {
        "id": 7,
        "question": "What problem does Seismic solve for institutional fintech adoption in Web3?",
        "options": ["A) Lack of colorful user interfaces", "B) The conflict between public ledger transparency and banking privacy laws", "C) High cost of physical hardware mining", "D) Slow internet connection speeds"],
        "correct_answer": "B"
    },
    {
        "id": 8,
        "question": "Can a neobank comply with global financial audits while using Seismic?",
        "options": ["A) No, because all data is completely deleted", "B) Yes, due to its compliance-friendly private framework", "C) Only if they use a centralized secondary server", "D) Only on weekends"],
        "correct_answer": "B"
    },
    {
        "id": 9,
        "question": "What is the main advantage of protocol-level encryption for fintechs?",
        "options": ["A) Faster website rendering", "B) Native data security without relying on fragmented third-party add-ons", "C) It turns all applications into mobile games", "D) Complete bypass of traditional banking firewalls"],
        "correct_answer": "B"
    },
    {
        "id": 10,
        "question": "Seismic's framework acts as a bridge between which two financial ecosystems?",
        "options": ["A) Barter systems and E-commerce", "B) Institutional Fintech/Neobanks and Decentralized Privacy Networks", "C) Corporate real estate and stock markets", "D) Traditional physical cash and gold reserves"],
        "correct_answer": "B"
    }
]

class AnswerCheckRequest(BaseModel):
    quiz_id: int
    user_answer: str

# 1. Sob gulo quiz eksathe pabar endpoint
@app.get("/api/quizzes")
def get_all_quizzes():
    return {"quizzes": SEISMIC_QUIZZES}

# 2. Id dhore specific quiz pabar endpoint (e.g., /api/quiz/1)
@app.get("/api/quiz/{quiz_id}")
def get_single_quiz(quiz_id: int):
    for quiz in SEISMIC_QUIZZES:
        if quiz["id"] == quiz_id:
            return quiz
    raise HTTPException(status_code=404, detail="Quiz not found. Choose an ID between 1 and 10.")

# 3. AI diye answer check o explanation deyar endpoint
@app.post("/api/check-answer")
def check_answer(data: AnswerCheckRequest):
    selected_quiz = None
    for quiz in SEISMIC_QUIZZES:
        if quiz["id"] == data.quiz_id:
            selected_quiz = quiz
            break
            
    if not selected_quiz:
        raise HTTPException(status_code=404, detail="Invalid Quiz ID.")
        
    is_correct = data.user_answer.strip().upper() == selected_quiz["correct_answer"]
    status_text = "Correct" if is_correct else "Incorrect"
    
    # OpenRouter call for dynamic AI explanation
    if OPENROUTER_API_KEY:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        prompt = (
            f"The question was: '{selected_quiz['question']}'. "
            f"The correct answer is {selected_quiz['correct_answer']}. "
            f"The user selected: '{data.user_answer}'. "
            f"Provide a brief 2-sentence explanation in professional tone why this is {status_text.lower()} based on Seismic network's privacy and compliance infrastructure."
        )
        payload = {
            "model": "meta-llama/llama-3-8b-instruct:free",
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
            explanation = response.json()['choices'][0]['message']['content']
        except Exception:
            explanation = f"The answer is {status_text}."
    else:
        explanation = f"The answer is {status_text}. (AI Explanation unavailable without API Key)"

    return {
        "correct": is_correct,
        "correct_answer": selected_quiz["correct_answer"],
        "explanation": explanation
    }

@app.get("/")
def home():
    return {"status": "Seismic 10-Quiz Bot API is running perfectly!"}
