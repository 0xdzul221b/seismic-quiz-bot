from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- COMPLETE INTEGRATED QUIZ STORAGE ---
SEISMIC_QUIZ_BANK = [
    {"id": 1, "question": "What is the primary focus of Seismic?", "options": ["A) Public gaming networks", "B) Privacy-preserving, compliance-friendly blockchain for fintech", "C) Decentralized storage for video streaming", "D) High-frequency NFT trading platforms"], "answer": "B) Privacy-preserving, compliance-friendly blockchain for fintech"},
    {"id": 2, "question": "Which domain extension must be used for the Seismic Name Service?", "options": ["A) .eth", "B) .sol", "C) .size", "D) .crypto"], "answer": "C) .size"},
    {"id": 3, "question": "How does Seismic handle compliance and privacy?", "options": ["A) By making all transactions fully public", "B) Through programmable privacy features and encrypted state infrastructure", "C) By banning neobanks", "D) By using centralized databases"], "answer": "B) Through programmable privacy features and encrypted state infrastructure"},
    {"id": 4, "question": "Seismic is designed to primarily benefit which sector?", "options": ["A) Traditional art galleries", "B) Fintech and neobanks", "C) E-commerce supply chains", "D) Decentralized social media memes"], "answer": "B) Fintech and neobanks"},
    {"id": 5, "question": "What core tech architecture does Seismic utilize for shielded records?", "options": ["A) Encrypted state infrastructure", "B) Unencrypted public ledgers", "C) Centralized SQL servers", "D) Proof-of-Work paper trails"], "answer": "A) Encrypted state infrastructure"}
]

PRISMAX_QUIZ_BANK = [
    {"id": 1, "question": "What is PrismaX?", "options": ["A) A crypto exchange", "B) A service layer for Physical AI", "C) A gaming platform", "D) A cloud provider"], "answer": "B) A service layer for Physical AI"},
    {"id": 2, "question": "What are the three core pillars of PrismaX?", "options": ["A) Compute, Storage, Network", "B) Data, Teleoperation, Models", "C) AI, Blockchain, Gaming", "D) Robots, NFTs, DeFi"], "answer": "B) Data, Teleoperation, Models"},
    {"id": 3, "question": "PrismaX mainly focuses on which type of AI?", "options": ["A) Generative AI", "B) Physical AI", "C) Social AI", "D) Financial AI"], "answer": "B) Physical AI"},
    {"id": 4, "question": "Which program did PrismaX join in 2026?", "options": ["A) Google Startups", "B) NVIDIA Inception Program", "C) AWS Activate", "D) Microsoft Founders Hub"], "answer": "B) NVIDIA Inception Program"},
    {"id": 5, "question": "What major challenge is PrismaX solving?", "options": ["A) Slow internet speeds", "B) Lack of robotics hardware", "C) Shortage of high-quality robotics data", "D) Cloud storage issues"], "answer": "C) Shortage of high-quality robotics data"}
]

@app.get("/get-quiz/{quiz_type}")
def get_quiz(quiz_type: str):
    if quiz_type == "seismic":
        bank = SEISMIC_QUIZ_BANK
    elif quiz_type == "prismax":
        bank = PRISMAX_QUIZ_BANK
    else:
        raise HTTPException(status_code=404, detail="Quiz module not found")
    
    sample_size = min(len(bank), 10)
    return {"status": "success", "total": sample_size, "quizzes": random.sample(bank, sample_size)}

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Welcome to Xdzul</title>
    <style>
        body {
            background: radial-gradient(circle at 10% 20%, rgba(237, 228, 213, 0.12) 0%, transparent 45%),
                        radial-gradient(circle at 90% 80%, rgba(149, 121, 91, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at center, #110e0c 0%, #050403 100%);
            background-color: #050403;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 100vh;
            margin: 0;
            padding: 30px 15px;
            box-sizing: border-box;
        }

        /* --- TOP LANDING FORMAT --- */
        .main-title {
            font-size: 26px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 25px;
            letter-spacing: 0.5px;
            text-align: center;
        }

        /* --- PRESERVATION OF NAVBAR TAB LAYOUT --- */
        .nav-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            width: 100%;
            max-width: 430px;
            margin-bottom: 30px;
        }
        .nav-item {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 14px;
            text-align: center;
            font-size: 14px;
            color: #b5b2ad;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            transition: all 0.2s ease;
        }
        .nav-item.active {
            background: rgba(45, 38, 36, 0.8);
            border-color: rgba(237, 228, 213, 0.2);
            color: #ffffff;
            box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);
        }

        /* --- NATIVE MAIN CARD MODULE --- */
        .quiz-card {
            background: rgba(22, 18, 16, 0.8);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 24px;
            padding: 28px;
            max-width: 430px;
            width: 100%;
            box-shadow: 0 30px 70px rgba(0, 0, 0, 0.85);
            border: 1px solid rgba(237, 228, 213, 0.05);
            box-sizing: border-box;
        }

        .header {
            text-align: center;
            margin-bottom: 24px;
        }
        .header h2 {
            font-size: 24px;
            margin: 0;
            color: #ffffff;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        .subtitle {
            font-size: 11px;
            color: #9c9893;
            background: rgba(255, 255, 255, 0.05);
            padding: 5px 12px;
            border-radius: 20px;
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }
        
        /* --- HUB LAYER SELECTION INSIDE CARD --- */
        .hub-container {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .hub-btn {
            background: rgba(36, 30, 27, 0.5);
            border: 1px solid rgba(237, 228, 213, 0.08);
            border-radius: 14px;
            padding: 18px;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .hub-btn:hover {
            background: rgba(149, 121, 91, 0.15);
            border-color: rgb(149, 121, 91);
            transform: translateY(-1px);
        }
        .hub-btn .title {
            font-size: 15px;
            font-weight: 700;
            color: rgb(237, 228, 213);
            margin-bottom: 4px;
        }
        .hub-btn .desc {
            font-size: 12px;
            color: #9c9893;
            line-height: 1.4;
        }

        /* --- ACTIVE TASK CONTROLS --- */
        .parameter-label {
            font-size: 11px;
            color: #9c9893;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            font-weight: 700;
        }
        .timer-bar-container {
            width: 100%;
            background: rgba(255, 255, 255, 0.04);
            height: 4px;
            border-radius: 2px;
            margin-bottom: 24px;
            overflow: hidden;
        }
        .timer-bar {
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            transition: width 1s linear;
        }
        .question {
            font-size: 16px;
            line-height: 1.5;
            margin-bottom: 24px;
            color: #f5f4f2;
            font-weight: 500;
        }
        .options-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .option-btn {
            background: rgba(36, 30, 27, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            color: #e5e3df;
            padding: 15px;
            border-radius: 12px;
            text-align: left;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .option-btn:hover {
            background: rgba(255, 255, 255, 0.03);
            border-color: rgba(237, 228, 213, 0.2);
        }
        .correct {
            background: rgba(46, 204, 113, 0.15) !important;
            border-color: #2ecc71 !important;
            color: #2ecc71 !important;
            font-weight: bold;
        }
        .wrong {
            background: rgba(231, 76, 60, 0.15) !important;
            border-color: #e74c3c !important;
            color: #e74c3c !important;
        }
        
        .timeout-alert {
            background: rgba(231, 76, 60, 0.1);
            border: 1px solid rgba(231, 76, 60, 0.2);
            border-radius: 12px;
            padding: 15px;
            margin-top: 20px;
            color: #ef9a9a;
            font-size: 13px;
            line-height: 1.4;
        }
        .timeout-alert strong {
            display: block;
            margin-bottom: 4px;
            text-transform: uppercase;
            font-size: 11px;
            letter-spacing: 0.5px;
        }

        .next-btn, .restart-btn {
            background: #ffffff;
            color: #050403;
            border: none;
            padding: 14px;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 700;
            width: 100%;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 20px;
            transition: opacity 0.2s ease;
        }
        .next-btn:disabled {
            opacity: 0.4;
            cursor: not-allowed;
        }
    </style>
</head>
<body>

    <div class="main-title">Welcome to Xdzul</div>

    <div class="nav-container">
        <div class="nav-item">🏠 Home</div>
        <div class="nav-item">🎨 Art</div>
        <div class="nav-item active">🛡️ Quiz</div>
        <div class="nav-item">📸 Photograph</div>
    </div>

    <div class="quiz-card" id="main-card">
        <div id="hub-view">
            <div class="header">
                <h2>Select Verification Hub</h2>
            </div>
            <div class="hub-container">
                <div class="hub-btn" onclick="initiateQuizModule('seismic')">
                    <div class="title">🔐 Seismic Quiz</div>
                    <div class="desc">Privacy-preserving compliance blockchain infrastructure verification setup.</div>
                </div>
                <div class="hub-btn" onclick="initiateQuizModule('prismax')">
                    <div class="title">🤖 PrismaX Quiz</div>
                    <div class="desc">Physical AI & decentralized data shielded robotic model parameters.</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let quizzes=[],currentIdx=0,score=0,timeLeft=15,timerInterval=null,canClick=true,isTabActive=true;
        let activeQuizType = '', selectedAnswer = null;
        const audioCtx=new(window.AudioContext||window.webkitAudioContext)();

        function playRobotSound(type) {
            try {
                let osc=audioCtx.createOscillator();
                let gain=audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                if(type==='correct') {
                    osc.type='triangle'; osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); 
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1); 
                    gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.2);
                } else if(type==='wrong') {
                    osc.type='sawtooth'; osc.frequency.setValueAtTime(130, audioCtx.currentTime); 
                    osc.frequency.linearRampToValueAtTime(60, audioCtx.currentTime + 0.3); 
                    gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.3);
                }
            } catch(e){}
        }

        async function initiateQuizModule(type) {
            activeQuizType = type;
            renderQuizSkeleton();
            try{
                let e=await fetch(`/get-quiz/\${type}`),t=await e.json();
                quizzes=t.quizzes,currentIdx=0,score=0;
                renderQuestion();
            }catch(e){
                document.getElementById("q-area").innerText="Failed to initialize pipeline parameters."
            }
        }

        function renderQuizSkeleton() {
            let title = activeQuizType === 'seismic' ? 'Seismic Systems' : 'PrismaX';
            let subtitle = activeQuizType === 'seismic' ? '🔒 COMPLIANCE ACTIVE | ⏱️ 0 S' : '🔒 PHYSICAL AI & DATA SHIELDED QUIZ';
            
            document.getElementById("main-card").innerHTML = `
                <div class="header">
                    <h2>\${title}</h2>
                    <div class="subtitle">\${subtitle}</div>
                </div>
                <div id="quiz-runtime">
                    <div class="parameter-label" id="param-track">PARAMETER 00 / 00</div>
                    <div class="timer-bar-container"><div class="timer-bar" id="t-bar"></div></div>
                    <div class="question" id="q-area">Loading active trace...</div>
                    <div class="options-container" id="opts-area"></div>
                    <div id="alert-space"></div>
                    <button class="next-btn" id="next-action" disabled onclick="advanceSequence()">Next Parameter</button>
                </div>`;
        }

        function startTimer(){
            clearInterval(timerInterval);
            timeLeft=15; canClick=true; updateTimerBar();
            timerInterval=setInterval(()=>{
                if(!isTabActive) return;
                timeLeft--; updateTimerBar();
                if(timeLeft<=0){ clearInterval(timerInterval); canClick=false; triggerTimeoutState() }
            },1000)
        }

        function updateTimerBar(){
            let el = document.getElementById("t-bar");
            if(el) el.style.width=(timeLeft/15)*100+"%";
        }

        function renderQuestion(){
            if(currentIdx >= quizzes.length){ showFinalAnalytics(); return }
            startTimer();
            selectedAnswer = null;
            document.getElementById("next-action").disabled = true;
            document.getElementById("alert-space").innerHTML = "";
            
            let q = quizzes[currentIdx];
            document.getElementById("param-track").innerText = `PARAMETER \${String(currentIdx+1).padStart(2, '0')} / \${String(quizzes.length).padStart(2, '0')}`;
            document.getElementById("q-area").innerText = q.question;
            
            let target = document.getElementById("opts-area");
            target.innerHTML = "";
            q.options.forEach(opt => {
                let btn = document.createElement("button");
                btn.className = "option-btn";
                btn.innerText = opt;
                btn.onclick = () => validateSelection(btn, opt, q.answer);
                target.appendChild(btn);
            });
        }

        function validateSelection(btn, val, correctAns){
            if(!canClick) return;
            clearInterval(timerInterval); canClick = false;
            
            let totalBtns = document.querySelectorAll(".option-btn");
            totalBtns.forEach(b => b.disabled = true);
            
            if(val === correctAns){
                btn.classList.add("correct");
                playRobotSound('correct');
                score++;
            } else {
                btn.classList.add("wrong");
                playRobotSound('wrong');
                totalBtns.forEach(b => { if(b.innerText === correctAns) b.classList.add("correct") });
            }
            document.getElementById("next-action").disabled = false;
        }

        function triggerTimeoutState(){
            playRobotSound('wrong');
            let correctAns = quizzes[currentIdx].answer;
            document.querySelectorAll(".option-btn").forEach(b => {
                b.disabled = true;
                if(b.innerText === correctAns) b.classList.add("correct"); else b.classList.add("wrong");
            });
            
            document.getElementById("alert-space").innerHTML = `
                <div class="timeout-alert">
                    <strong>⏰ VERIFICATION TIMEOUT</strong>
                    Security validation link expired. System flagged this session trace as unverified.
                </div>`;
            document.getElementById("next-action").disabled = false;
        }

        function advanceSequence(){
            currentIdx++;
            renderQuestion();
        }

        function showFinalAnalytics(){
            clearInterval(timerInterval);
            document.getElementById("main-card").innerHTML = `
                <div style="text-align:center; padding: 10px 0;">
                    <h2 style="color:rgb(237, 228, 213); font-size:22px; margin-bottom:8px;">Session Terminated</h2>
                    <div class="subtitle" style="margin-bottom:25px;">Trace Status: Logged</div>
                    <p style="font-size:26px; color:#ffffff; font-weight:800; margin-bottom:30px;">Verification Score: \${score} / \${quizzes.length}</p>
                    <button class="restart-btn" style="background:linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));" onclick="location.reload()">Return to Dashboard</button>
                </div>`;
        }

        document.addEventListener("visibilitychange", () => {
            isTabActive = !document.hidden;
        });
    </script>
</body>
</html>"""
    return html_content
