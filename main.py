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
        <title>Xdzul Terminal Hub</title>
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;600&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }
            body {
                background: radial-gradient(circle at 50% 0%, #1c192e 0%, #0d0b12 100%);
                color: #f8fafc; min-height: 100vh; display: flex; overflow: hidden;
            }

            /* Left Sidebar Layout Navigation Area (Home, Art, Quiz, Photograph) */
            .sidebar {
                width: 260px; background: rgba(255, 255, 255, 0.02);
                border-right: 1px solid rgba(255, 255, 255, 0.06);
                padding: 40px 24px; display: flex; flex-direction: column; gap: 40px;
                backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
            }
            .brand { font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; color: #fff; letter-spacing: 0.5px; }
            .nav-links { display: flex; flex-direction: column; gap: 12px; }
            .nav-item {
                display: flex; align-items: center; gap: 14px; padding: 14px 18px;
                border-radius: 12px; color: #94a3b8; font-size: 14px; font-weight: 600;
                cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); border: 1px solid transparent;
            }
            .nav-item:hover { color: #fff; background: rgba(255, 255, 255, 0.04); }
            .nav-item.active {
                color: #fff; background: rgba(255, 255, 255, 0.05);
                border-color: rgba(255, 255, 255, 0.1); box-shadow: inset 0 1px 0 rgba(255,255,255,0.1);
            }
            .nav-item .icon { font-size: 18px; }

            /* Right Content Main View Pane */
            .main-content { flex: 1; padding: 40px; overflow-y: auto; display: flex; justify-content: center; align-items: center; position: relative; }
            .content-tab { display: none; width: 100%; max-width: 520px; animation: fadeIn 0.5s ease; }
            .content-tab.active { display: block; }

            @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

            /* Premium Dark Hub Card Dashboard Core */
            .hub-card {
                background: rgba(43, 33, 38, 0.55); border: 1px solid rgba(255, 255, 255, 0.12);
                padding: 40px 32px; border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
                backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); width: 100%;
            }
            h1 { font-family: 'Space Grotesk', sans-serif; font-size: 26px; font-weight: 700; color: #fff; margin-bottom: 8px; text-align: center; }
            .subtitle { font-size: 13px; color: #bfa0ac; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; margin-bottom: 25px; text-align: center; line-height: 1.4; }
            p { color: #dfd5da; font-size: 14px; line-height: 1.6; }

            /* Dynamic Built-in Quiz Engine Interfaces */
            .brand-header { display: flex; flex-direction: column; align-items: center; margin-bottom: 24px; }
            .badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); padding: 6px 14px; border-radius: 100px; font-size: 11px; font-weight: 600; color: #dfd5da; margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
            .progress-wrapper { width: 100%; background: rgba(255,255,255,0.05); height: 6px; border-radius: 100px; margin-bottom: 24px; }
            .progress-bar { height: 100%; width: 10%; background: linear-gradient(90deg, #bfa0ac, #e5d5db); border-radius: 100px; transition: width 0.4s ease; }
            .question-box { margin-bottom: 24px; }
            .question-number { font-size: 12px; font-weight: 700; color: #bfa0ac; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
            .question-text { font-size: 16px; font-weight: 600; line-height: 1.5; color: #ffffff; }
            .options-grid { display: flex; flex-direction: column; gap: 12px; }
            .option-card { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); padding: 16px; border-radius: 14px; color: #e2e8f0; font-size: 14px; text-align: left; cursor: pointer; width: 100%; outline: none; transition: all 0.2s; }
            .option-card:hover { background: rgba(255, 255, 255, 0.06); border-color: rgba(255, 255, 255, 0.25); transform: translateY(-2px); }
            .feedback-panel { margin-top: 20px; padding: 16px; border-radius: 14px; display: none; font-size: 13px; line-height: 1.5; }
            .feedback-panel.correct { background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); color: #a7f3d0; }
            .feedback-panel.incorrect { background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.25); color: #fca5a5; }
            .feedback-title { font-weight: 700; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
            .action-btn { margin-top: 20px; width: 100%; background: #ffffff; color: #2b2126; border: none; padding: 16px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; display: none; font-family: 'Space Grotesk', sans-serif; text-transform: uppercase; letter-spacing: 0.5px; }
            
            /* Photo Gallery Preview grid styles */
            .photo-placeholder {
                background: rgba(255,255,255,0.02); border: 1px dashed rgba(255,255,255,0.1); 
                padding: 40px; border-radius: 16px; text-align: center; color: #94a3b8; font-size: 13px;
            }

            @media(max-width: 768px) {
                body { flex-direction: column; overflow: auto; }
                .sidebar { width: 100%; border-right: none; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 20px; gap: 20px; }
                .nav-links { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }
                .nav-item { padding: 12px; font-size: 13px; justify-content: center; }
                .main-content { padding: 20px; min-height: calc(100vh - 180px); }
            }
        </style>
    </head>
    <body>

        <div class="sidebar">
            <div class="brand">Welcome to Xdzul</div>
            <div class="nav-links">
                <div class="nav-item active" onclick="switchTab('home-tab', this)">
                    <span class="icon">🏠</span> <span>Home</span>
                </div>
                <div class="nav-item" onclick="switchTab('art-tab', this)">
                    <span class="icon">🎨</span> <span>Art</span>
                </div>
                <div class="nav-item" onclick="switchTab('quiz-tab', this)">
                    <span class="icon">🛡️</span> <span>Quiz</span>
                </div>
                <div class="nav-item" onclick="switchTab('photo-tab', this)">
                    <span class="icon">📸</span> <span>Photograph</span>
                </div>
            </div>
        </div>

        <div class="main-content">
            
            <div id="home-tab" class="content-tab active">
                <div class="hub-card">
                    <h1>Welcome to Xdzul’s Hub</h1>
                    <div class="subtitle">✨ Unlocking the next level of entertainment. Art, quizzes, photography...everything you need to check.</div>
                    <p style="text-align: center; color: #dfd5da; margin-top: 15px;">Left block configuration control list runtime utilize kore custom segments explore tracking active korun.</p>
                </div>
            </div>

            <div id="art-tab" class="content-tab">
                <div class="hub-card">
                    <h1>Art Matrix Collection</h1>
                    <div class="subtitle">🎨 Visual Artifact Hub</div>
                    <p style="margin-bottom: 20px; text-align: center;">Ekhane apnar custom character concepts, digital models, dynamic graphics pipeline tracking render pipelines display hobe.</p>
                    <div class="photo-placeholder">
                        🖼️ Asset repository stream offline. Integrating render pipelines core...
                    </div>
                </div>
            </div>

            <div id="quiz-tab" class="content-tab">
                <div class="hub-card">
                    <div class="brand-header">
                        <h1>Seismic Systems</h1>
                        <div class="badge" id="badge-status">🔒 Compliance Active | ⏱️ <span id="timer-display">20</span>s</div>
                    </div>
                    
                    <div class="progress-wrapper">
                        <div class="progress-bar" id="progress"></div>
                    </div>
                    
                    <div class="question-box">
                        <div class="question-number" id="q-num">Parameter 01 / 10</div>
                        <div class="question-text" id="question">Initializing terminal environment tracking protocols...</div>
                    </div>
                    
                    <div class="options-grid" id="options"></div>
                    <div class="feedback-panel" id="feedback"></div>
                    <button class="action-btn" id="action-btn" onclick="loadNextQuiz()">Next Parameter</button>
                </div>
            </div>

            <div id="photo-tab" class="content-tab">
                <div class="hub-card">
                    <h1>Photographic Archives</h1>
                    <div class="subtitle">📸 Captured Logs Matrix</div>
                    <p style="margin-bottom: 20px; text-align: center;">Ekhane apnar captured imagery snapshots, visual travel logs, environment frames sync updates stream thakbe.</p>
                    <div class="photo-placeholder">
                        📷 Media database interface offline. Initializing secure bucket routes...
                    </div>
                </div>
            </div>

        </div>

        <script>
            let currentQuizId = 1;
            let userScore = 0;
            let timerInterval;
            let timeLeft = 20;

            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            function playSound(type) {
                try {
                    const osc = audioCtx.createOscillator();
                    const gain = audioCtx.createGain();
                    osc.connect(gain); gain.connect(audioCtx.destination);
                    if (type === 'correct') {
                        osc.type = 'sine'; osc.frequency.setValueAtTime(600, audioCtx.currentTime);
                        osc.frequency.exponentialRampToValueAtTime(1200, audioCtx.currentTime + 0.15);
                        gain.gain.setValueAtTime(0.15, audioCtx.currentTime); osc.start(); osc.stop(audioCtx.currentTime + 0.15);
                    } else if (type === 'incorrect') {
                        osc.type = 'sawtooth'; osc.frequency.setValueAtTime(180, audioCtx.currentTime);
                        osc.frequency.linearRampToValueAtTime(90, audioCtx.currentTime + 0.25);
                        gain.gain.setValueAtTime(0.2, audioCtx.currentTime); osc.start(); osc.stop(audioCtx.currentTime + 0.25);
                    }
                } catch (e) {}
            }

            // Clean View Tab Routing Matrix Controller
            function switchTab(tabId, element) {
                document.querySelectorAll('.content-tab').forEach(tab => tab.classList.remove('active'));
                document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
                
                document.getElementById(tabId).classList.add('active');
                element.classList.add('active');
                
                // Keep the state of the ticking parameter engine clock locked when switching windows
                if (tabId !== 'quiz-tab') {
                    clearInterval(timerInterval);
                } else if(currentQuizId <= 10) {
                    startTimer();
                }
            }

            function startTimer() {
                clearInterval(timerInterval);
                timeLeft = 20;
                const bDisplay = document.getElementById('badge-status');
                if(bDisplay) bDisplay.innerHTML = `🔒 Compliance Active | ⏱️ <span id="timer-display">${timeLeft}</span>s`;

                timerInterval = setInterval(() => {
                    timeLeft--;
                    const tSpan = document.getElementById('timer-display');
                    if(tSpan) tSpan.innerText = timeLeft;
                    
                    if (timeLeft <= 0) {
                        clearInterval(timerInterval);
                        autoTimeoutAnswer();
                    }
                }, 1000);
            }

            async function loadQuiz(id) {
                const feedbackDiv = document.getElementById('feedback');
                const actionBtn = document.getElementById('action-btn');
                if(feedbackDiv) feedbackDiv.style.display = 'none';
                if(actionBtn) actionBtn.style.display = 'none';
                
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
                    
                    if(document.getElementById('quiz-tab').classList.contains('active')) {
                        startTimer();
                    }
                } catch (err) {
                    showCompletionScreen();
                }
            }

            function autoTimeoutAnswer() {
                const buttons = document.querySelectorAll('.option-card');
                buttons.forEach(b => b.disabled = true);
                playSound('incorrect');

                const feedbackDiv = document.getElementById('feedback');
                feedbackDiv.className = 'feedback-panel incorrect';
                feedbackDiv.style.display = 'block';
                feedbackDiv.innerHTML = '<div class="feedback-title">⏰ Verification Timeout</div>Security validation link expired. System flagged this session trace as unverified.';
                document.getElementById('action-btn').style.display = 'block';
            }

            async function submitAnswer(id, selectedLetter) {
                clearInterval(timerInterval);
                const buttons = document.querySelectorAll('.option-card');
                buttons.forEach(b => b.disabled = true);
                
                const feedbackDiv = document.getElementById('feedback');
                feedbackDiv.className = 'feedback-panel';
                feedbackDiv.style.display = 'block';
                feedbackDiv.innerHTML = '<div class="feedback-title">Verification Core</div>Decrypting network execution logs via OpenRouter cloud architecture...';

                try {
                    const baseUrl = window.location.origin;
                    const res = await fetch(`${baseUrl}/api/check-answer`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ quiz_id: id, user_answer: selectedLetter })
                    });
                    const result = await res.json();
                    
                    if(result.correct) {
                        userScore++; playSound('correct');
                        feedbackDiv.className = 'feedback-panel correct';
                        feedbackDiv.innerHTML = `<div class="feedback-title">✓ Shield Approved</div>${result.explanation}`;
                    } else {
                        playSound('incorrect');
                        feedbackDiv.className = 'feedback-panel incorrect';
                        feedbackDiv.innerHTML = `<div class="feedback-title">✗ Verification Blocked</div>Correct Node Target: <strong>${result.correct_answer}</strong>.<br>${result.explanation}`;
                    }
                } catch(e) {
                    feedbackDiv.className = 'feedback-panel incorrect';
                    feedbackDiv.innerHTML = '<div class="feedback-title">System Execution Fault</div>Failed to establish stable verification path channels.';
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

            function shareOnX() {
                const tweetText = encodeURIComponent(`🔒 Just secured my node protocols on the @SeismicNetwork compliance terminal! 🛡️ Final Score: ${userScore}/10.\n\nCan you decrypt the stack? Test your Web3 security IQ here:`);
                const shareUrl = encodeURIComponent(window.location.href);
                window.open(`https://twitter.com/intent/tweet?text=${tweetText}&url=${shareUrl}`, '_blank');
            }

            function showCompletionScreen() {
                clearInterval(timerInterval);
                document.getElementById('progress').style.width = '100%';
                document.getElementById('q-num').innerText = "Session Terminal Completed";
                
                let performanceMatrix = "";
                if(userScore >= 8) performanceMatrix = "🏅 Exceptional performance! You have high-tier cryptographic access credentials clearance.";
                else if(userScore >= 5) performanceMatrix = "⚡ Fair operational comprehension. Protocol optimization parameters recommended.";
                else performanceMatrix = "⚠️ Critical security protocol vulnerabilities detected. Review node specifications.";

                document.getElementById('question').innerHTML = `
                    <div style="text-align: center; margin-top: 10px;">
                        <span style="font-size: 40px;">🛡️</span>
                        <h2 style="font-size: 18px; color: #fff; margin: 12px 0 6px 0; font-family: 'Space Grotesk', sans-serif;">SESSION REPORT SYNCED</h2>
                        <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); padding: 16px; border-radius: 14px; margin: 16px 0;">
                            <p style="font-size: 12px; color: #bfa0ac; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">Verified Integrity Metrics</p>
                            <p style="font-size: 30px; font-weight: 700; color: #ffffff; font-family: 'Space Grotesk', sans-serif;">${userScore} <span style="font-size: 16px; color: #76646e;">/ 10</span></p>
                        </div>
                        <p style="font-size: 13px; line-height: 1.5; color: #dfd5da; margin-bottom: 20px;">${performanceMatrix}</p>
                        <button onclick="shareOnX()" style="width: 100%; background: #1d9bf0; color: #fff; border: none; padding: 14px; border-radius: 12px; font-size: 13px; font-weight: 700; cursor: pointer; text-transform: uppercase; font-family: 'Space Grotesk', sans-serif; margin-bottom: 12px;">🐦 Share Metrics on X</button>
                        <button onclick="window.location.reload()" style="width: 100%; background: transparent; border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 14px; border-radius: 12px; font-size: 12px; font-weight: 600; cursor: pointer; text-transform: uppercase;">Re-verify Terminal Stack</button>
                    </div>
                `;
                document.getElementById('options').innerHTML = '';
                document.getElementById('feedback').style.display = 'none';
                document.getElementById('action-btn').style.display = 'none';
            }

            // Start running parameters
            loadQuiz(currentQuizId);
        </script>
    </body>
    </html>
    """
    return html_content
