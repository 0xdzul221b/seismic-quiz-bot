import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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

@app.get("/api/quizzes")
def get_all_quizzes():
    return {"quizzes": SEISMIC_QUIZZES}

@app.get("/api/quiz/{quiz_id}")
def get_single_quiz(quiz_id: int):
    for quiz in SEISMIC_QUIZZES:
        if quiz["id"] == quiz_id:
            return quiz
    raise HTTPException(status_code=404, detail="Quiz not found.")

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
        explanation = f"The answer is {status_text}. (AI Explanation unavailable)"

    return {
        "correct": is_correct,
        "correct_answer": selected_quiz["correct_answer"],
        "explanation": explanation
    }

# Premium HTML Web UI Response for Root Path
@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Seismic Systems | Shielded Quiz Bot</title>
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }
            
            /* Seismic Official Inspired Dark Ambient Background Setup */
            body {
    background: radial-gradient(circle at 50% 0%, #161920 0%, #0d0f12 70%);
    color: #e2e8f0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    overflow-x: hidden;
}
            
            /* Matrix Grid Mesh Pattern Effect */
            body::before {
                content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background-image: linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
                background-size: 30px 30px; z-index: -1; pointer-events: none;
            }

            .container { 
                max-width: 550px; width: 100%; 
                background: rgba(43, 33, 38, 0.75);
                border: 1px solid rgba(255, 255, 255, 0.07); 
                border-radius: 16px; padding: 30px; 
                box-shadow: 0 20px 40px rgba(0,0,0,0.5);
                backdrop-filter: blur(12px);
                position: relative;
            }

            /* Neon Shield Accent Indicator */
            .container::before {
                content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
                background: linear-gradient(90deg, #3b82f6, #10b981);
                border-radius: 16px 16px 0 0;
            }

            h1 { font-size: 24px; font-weight: 700; margin-bottom: 8px; text-align: center; color: #fff; letter-spacing: -0.5px; }
            .subtitle { font-size: 13px; color: #94a3b8; text-align: center; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 1px; }
            
            .quiz-box { display: block; }
            .question-text { font-size: 16px; font-weight: 600; margin-bottom: 20px; line-height: 1.5; color: #f1f5f9; }
            
            .options-container { display: flex; flex-direction: column; gap: 12px; }
            .option-btn { 
                background: rgba(255, 255, 255, 0.03); 
                border: 1px solid rgba(255, 255, 255, 0.08); 
                padding: 14px 18px; border-radius: 10px; 
                color: #cbd5e1; font-size: 14px; text-align: left; 
                cursor: pointer; transition: all 0.2s ease; 
            }
            .option-btn:hover { background: rgba(59, 130, 246, 0.1); border-color: rgba(59, 130, 246, 0.4); color: #fff; }
            
            .feedback-box { margin-top: 20px; padding: 15px; border-radius: 10px; display: none; font-size: 14px; line-height: 1.5; }
            .feedback-box.correct { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: #34d399; }
            .feedback-box.incorrect { background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #f87171; }
            
            .next-btn { 
                margin-top: 20px; width: 100%; background: #3b82f6; color: white; border: none; 
                padding: 14px; border-radius: 10px; font-weight: 600; cursor: pointer; display: none; transition: background 0.2s;
            }
            .next-btn:hover { background: #2563eb; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SEISMIC SYSTEMS</h1>
            <div class="subtitle">🔒 Compliance & Privacy Shielded Quiz</div>
            
            <div class="quiz-box">
                <div class="question-text" id="question">Loading dynamic hardware parameters...</div>
                <div class="options-container" id="options"></div>
                <div class="feedback-box" id="feedback"></div>
                <button class="next-btn" id="next-btn" onclick="loadNextQuiz()">Next Parameter →</button>
            </div>
        </div>

        <script>
            let currentQuizId = 1;

            async function loadQuiz(id) {
                document.getElementById('feedback').style.display = 'none';
                document.getElementById('next-btn').style.display = 'none';
                
                try {
                    const response = await fetch(`/api/quiz/${id}`);
                    const quiz = await response.json();
                    
                    document.getElementById('question').innerText = `Q${quiz.id}. ${quiz.question}`;
                    const optionsDiv = document.getElementById('options');
                    optionsDiv.innerHTML = '';
                    
                    quiz.options.forEach(opt => {
                        const btn = document.createElement('button');
                        btn.className = 'option-btn';
                        btn.innerText = opt;
                        btn.onclick = () => submitAnswer(quiz.id, opt.charAt(0));
                        optionsDiv.appendChild(btn);
                    });
                } catch (err) {
                    document.getElementById('question').innerText = "All 10 cryptographic parameters successfully mapped!";
                    document.getElementById('options').innerHTML = "";
                }
            }

            async function submitAnswer(id, selectedLetter) {
                const buttons = document.querySelectorAll('.option-btn');
                buttons.forEach(b => b.disabled = true);
                
                const feedbackDiv = document.getElementById('feedback');
                feedbackDiv.className = 'feedback-box';
                feedbackDiv.style.display = 'block';
                feedbackDiv.innerText = "Decrypting verification flow from OpenRouter infrastructure...";

                const res = await fetch('/api/check-answer', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ quiz_id: id, user_answer: selectedLetter })
                });
                const result = await res.json();
                
                if(result.correct) {
                    feedbackDiv.classList.add('correct');
                    feedbackDiv.innerText = "✓ Shield Verification Success! " + result.explanation;
                } else {
                    feedbackDiv.classList.add('incorrect');
                    feedbackDiv.innerText = "✗ Verification Blocked. Correct Answer: " + result.correct_answer + ". " + result.explanation;
                }
                
                document.getElementById('next-btn').style.display = 'block';
            }

            function loadNextQuiz() {
                currentQuizId++;
                if(currentQuizId <= 10) {
                    loadQuiz(currentQuizId);
                } else {
                    document.getElementById('question').innerText = "🔒 Session Cleared: You have successfully mastered Seismic infrastructure's full privacy compliance deck!";
                    document.getElementById('options').innerHTML = '';
                    document.getElementById('feedback').style.display = 'none';
                    document.getElementById('next-btn').style.display = 'none';
                }
            }

            // Initialization
            loadQuiz(currentQuizId);
        </script>
    </body>
    </html>
    """
    return html_content
