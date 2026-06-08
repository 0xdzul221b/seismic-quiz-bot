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
# Fully Optimized Premium Cyberpunk Web UI Response for Root Path
@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Seismic Network | Institutional Quiz Shield</title>
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            
                    body { 
            background: radial-gradient(circle at 50% 0%, #8c737e 0%, #6e5560 50%, #2b2126 100%);
            color: #f8fafc; 
            font-family: 'Plus Jakarta Sans', sans-serif;
            min-height: 100vh; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: flex-start;
            padding: 0;
            overflow-x: hidden;
            position: relative;
        }
        
        /* High-Tech Glowing Backdrop Elements */
        body::before {
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
            background-size: 24px 24px; z-index: 0; pointer-events: none;
        }

        .container { 
            width: 100%; 
            max-width: 100%; 
            min-height: 100vh; 
            background: rgba(43, 33, 38, 0.55); 
            border: none; 
            border-radius: 0; 
            padding: 40px 24px; 
            box-shadow: none;
            backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
            display: flex;
            flex-direction: column;
            z-index: 10;
        }
            .container::before {
                content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
                background: linear-gradient(90deg, #bfa0ac, #6e5560, #4f3b44);
                border-radius: 24px 24px 0 0;
            }

            /* Header Badges */
            .brand-header { display: flex; flex-direction: column; align-items: center; margin-bottom: 24px; }
            h1 { font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; color: #fff; letter-spacing: 1px; text-transform: uppercase; }
            
            .badge {
                display: inline-flex; align-items: center; gap: 6px;
                background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 6px 12px; border-radius: 100px; font-size: 11px; font-weight: 600;
                color: #dfd5da; margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px;
            }

            /* Progress Bar Tracker */
            .progress-wrapper { width: 100%; background: rgba(255, 255, 255, 0.05); height: 6px; border-radius: 100px; margin-bottom: 24px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.03); }
            .progress-bar { height: 100%; width: 10%; background: linear-gradient(90deg, #bfa0ac, #e5d5db); border-radius: 100px; transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1); }

            /* Question Frame */
            .question-box { margin-bottom: 24px; }
            .question-number { font-size: 12px; font-weight: 700; color: #bfa0ac; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px; }
            .question-text { font-size: 16px; font-weight: 600; line-height: 1.5; color: #ffffff; }
            
            /* Sleek Interactive Option Buttons */
            .options-grid { display: flex; flex-direction: column; gap: 12px; }
            .option-card { 
                background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); 
                padding: 16px; border-radius: 14px; color: #e2e8f0; font-size: 14px; font-weight: 500;
                text-align: left; cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                width: 100%; outline: none; -webkit-tap-highlight-color: transparent;
            }
            .option-card:hover { 
                background: rgba(255, 255, 255, 0.06); border-color: rgba(255, 255, 255, 0.25);
                transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            .option-card:active { transform: translateY(0); }
            
            /* Professional Feedback Framework */
            .feedback-panel { margin-top: 20px; padding: 16px; border-radius: 14px; display: none; font-size: 13px; line-height: 1.6; animation: slideUp 0.3s ease; }
            .feedback-panel.correct { background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); color: #34d399; }
            .feedback-panel.incorrect { background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.25); color: #f87171; }
            .feedback-title { font-weight: 700; margin-bottom: 4px; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }

            /* Premium Action Trigger */
            .action-btn { 
                margin-top: 20px; width: 100%; background: #ffffff; color: #2b2126; border: none; 
                padding: 16px; border-radius: 14px; font-weight: 700; font-size: 14px; cursor: pointer; 
                display: none; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                font-family: 'Space Grotesk', sans-serif; text-transform: uppercase; letter-spacing: 0.5px;
            }
            .action-btn:hover { background: #e5d5db; transform: scale(1.01); }

            @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
            @keyframes slideUp { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="brand-header">
                <h1>Seismic Systems</h1>
                <div class="badge">🔒 Compliance Layer Active</div>
            </div>

            <div class="progress-wrapper">
                <div class="progress-bar" id="progress"></div>
            </div>
            
            <div class="question-box">
                <div class="question-number" id="q-num">Parameter 01 / 10</div>
                <div class="question-text" id="question">Initializing secure data node tracking...</div>
            </div>

            <div class="options-grid" id="options"></div>
            <div class="feedback-panel" id="feedback"></div>
            <button class="action-btn" id="action-btn" onclick="loadNextQuiz()">Next Parameter →</button>
        </div>

        <script>
            let currentQuizId = 1;

            async function loadQuiz(id) {
                const feedbackDiv = document.getElementById('feedback');
                const actionBtn = document.getElementById('action-btn');
                if(feedbackDiv) feedbackDiv.style.display = 'none';
                if(actionBtn) actionBtn.style.display = 'none';
                
                // Progress calculations update
                document.getElementById('progress').style.width = `${id * 10}%`;
                document.getElementById('q-num').innerText = `Parameter 0${id} / 10`;
                
                try {
                    const baseUrl = window.location.origin;
                    const response = await fetch(`${baseUrl}/api/quiz/${id}`);
                    if (!response.ok) throw new Error();
                    
                    const quiz = await response.json();
                    document.getElementById('question').innerText = quiz.question;
                    
                    const optionsDiv = document.getElementById('options');
                    optionsDiv.innerHTML = '';
                    
                    quiz.options.forEach(opt => {
                        const btn = document.createElement('button');
                        btn.className = 'option-card';
                        btn.innerText = opt;
                        btn.onclick = () => submitAnswer(quiz.id, opt.charAt(0));
                        optionsDiv.appendChild(btn);
                    });
                } catch (err) {
                    showCompletionScreen();
                }
            }

     async function submitAnswer(id, selectedLetter) {
                const buttons = document.querySelectorAll('.option-card');
                buttons.forEach(b => b.disabled = true);
                
                const feedbackDiv = document.getElementById('feedback');
                feedbackDiv.className = 'feedback-panel';
                feedbackDiv.style.display = 'block';
                feedbackDiv.innerHTML = '<div class="feedback-title">Verification Engine</div>Decrypting execution trace via OpenRouter infrastructure...';

                try {
                    const baseUrl = window.location.origin;
                    const res = await fetch(`${baseUrl}/api/check-answer`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ quiz_id: id, user_answer: selectedLetter })
                    });
                    const result = await res.json();
                    
                    if(result.correct) {
                        feedbackDiv.classList.add('correct');
                        feedbackDiv.innerHTML = `<div class="feedback-title">✓ Shield Approved</div>${result.explanation}`;
                    } else {
                        feedbackDiv.classList.add('incorrect');
                        feedbackDiv.innerHTML = `<div class="feedback-title">✗ Verification Blocked</div>Correct Path Option: <strong>${result.correct_answer}</strong>.<br>${result.explanation}`;
                    }
                } catch(e) {
                    feedbackDiv.classList.add('incorrect');
                    feedbackDiv.innerHTML = '<div class="feedback-title">System Error</div>Failed to securely check parameters.';
                }
                document.getElementById('action-btn').style.display = 'block';
            }

            function loadNextQuiz() {
                currentQuizId++;
                if(currentQuizId <= 10) {
                    loadQuiz(currentQuizId);
                } else {
                    showCompletionScreen();
                }
            }

            function showCompletionScreen() {
                document.getElementById('progress').style.width = '100%';
                document.getElementById('q-num').innerText = "Session Terminal Clear";
                document.getElementById('question').innerText = "🔒 You have successfully verified and mastered Seismic infrastructure's full privacy compliance parameters!";
                document.getElementById('options').innerHTML = '';
                document.getElementById('feedback').style.display = 'none';
                document.getElementById('action-btn').style.display = 'none';
            }

            loadQuiz(currentQuizId);
        </script>
    </body>
    </html>
    """
    return html_content
