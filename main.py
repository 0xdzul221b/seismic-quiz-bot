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

# --- QUIZ BANKS ---
SEISMIC_QUIZ_BANK = [
    {"id": 1, "question": "What is the primary focus of Seismic?", "options": ["Public gaming networks", "Privacy-preserving, compliance-friendly blockchain for fintech", "Decentralized storage for video streaming", "High-frequency NFT trading platforms"], "answer": "Privacy-preserving, compliance-friendly blockchain for fintech"},
    {"id": 2, "question": "Which domain extension must be used for the Seismic Name Service?", "options": [".eth", ".sol", ".size", ".crypto"], "answer": ".size"},
    {"id": 3, "question": "How does Seismic handle compliance and privacy?", "options": ["By making all transactions fully public", "Through programmable privacy features and encrypted state infrastructure", "By banning neobanks", "By using centralized databases"], "answer": "Through programmable privacy features and encrypted state infrastructure"},
    {"id": 4, "question": "Seismic is designed to primarily benefit which sector?", "options": ["Traditional art galleries", "Fintech and neobanks", "E-commerce supply chains", "Decentralized social media memes"], "answer": "Fintech and neobanks"},
    {"id": 5, "question": "What core tech architecture does Seismic utilize for shielded records?", "options": ["Encrypted state infrastructure", "Unencrypted public ledgers", "Centralized SQL servers", "Proof-of-Work paper trails"], "answer": "Encrypted state infrastructure"}
]

PRISMAX_QUIZ_BANK = [
    {"id": 1, "question": "What is PrismaX?", "options": ["A crypto exchange", "A service layer for Physical AI", "A gaming platform", "A cloud provider"], "answer": "A service layer for Physical AI"},
    {"id": 2, "question": "What are the three core pillars of PrismaX?", "options": ["Compute, Storage, Network", "Data, Teleoperation, Models", "AI, Blockchain, Gaming", "Robots, NFTs, DeFi"], "answer": "Data, Teleoperation, Models"},
    {"id": 3, "question": "PrismaX mainly focuses on which type of AI?", "options": ["Generative AI", "Physical AI", "Social AI", "Financial AI"], "answer": "Physical AI"},
    {"id": 4, "question": "Which program did PrismaX join in 2026?", "options": ["Google Startups", "NVIDIA Inception Program", "AWS Activate", "Microsoft Founders Hub"], "answer": "NVIDIA Inception Program"},
    {"id": 5, "question": "What major challenge is PrismaX solving?", "options": ["Slow internet speeds", "Lack of robotics hardware", "Shortage of high-quality robotics data", "Cloud storage issues"], "answer": "Shortage of high-quality robotics data"}
]

@app.get("/get-quiz/{quiz_type}")
def get_quiz(quiz_type: str):
    if quiz_type == "seismic":
        bank = SEISMIC_QUIZ_BANK
    elif quiz_type == "prismax":
        bank = PRISMAX_QUIZ_BANK
    else:
        raise HTTPException(status_code=404, detail="Quiz type not found")
    
    sample_size = min(len(bank), 10)
    return {"status": "success", "total": sample_size, "quizzes": random.sample(bank, sample_size)}

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Xdzul | Quiz Portal</title>
    <style>
        body {
            background: radial-gradient(circle at 10% 20%, rgba(237, 228, 213, 0.12) 0%, transparent 45%),
                        radial-gradient(circle at 90% 80%, rgba(149, 121, 91, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at center, #110e0c 0%, #050403 100%);
            background-color: #050403;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 15px;
            box-sizing: border-box;
            overflow: hidden;
        }
        
        .quiz-card {
            background: rgba(20, 16, 14, 0.75);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border-radius: 16px;
            padding: 28px;
            max-width: 430px;
            width: 100%;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
            position: relative;
            border: 1px solid rgba(237, 228, 213, 0.06);
        }
        
        .quiz-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            border-radius: 16px 16px 0 0;
        }
        
        .header {
            text-align: center;
            margin-bottom: 25px;
        }
        .header h2 {
            letter-spacing: 2px;
            font-size: 22px;
            margin: 0;
            color: rgb(237, 228, 213);
            text-transform: uppercase;
            font-weight: 800;
        }
        .subtitle {
            font-size: 11px;
            color: rgba(237, 228, 213, 0.6);
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }
        
        /* Hub Selection Styles */
        .hub-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-top: 10px;
        }
        .hub-btn {
            background: rgba(36, 30, 27, 0.6);
            border: 1px solid rgba(237, 228, 213, 0.1);
            border-radius: 12px;
            padding: 20px;
            text-align: left;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .hub-btn:hover {
            background: rgba(149, 121, 91, 0.2);
            border-color: rgb(149, 121, 91);
            transform: translateY(-2px);
        }
        .hub-btn .title {
            font-size: 16px;
            font-weight: 700;
            color: rgb(237, 228, 213);
        }
        .hub-btn .desc {
            font-size: 12px;
            color: #b5b2ad;
        }

        /* Active Quiz Styles */
        .timer-bar-container {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            height: 5px;
            border-radius: 3px;
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
            line-height: 1.6;
            margin-bottom: 24px;
            color: #f5f4f2;
        }
        .options-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .option-btn {
            background: rgba(36, 30, 27, 0.6);
            border: 1px solid rgba(237, 228, 213, 0.1);
            color: #e5e3df;
            padding: 15px;
            border-radius: 10px;
            text-align: left;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .option-btn:hover {
            background: rgba(149, 121, 91, 0.15);
            border-color: rgba(237, 228, 213, 0.3);
        }
        .correct {
            background: rgba(46, 204, 113, 0.2) !important;
            border-color: #2ecc71 !important;
            color: #2ecc71 !important;
            font-weight: bold;
        }
        .wrong {
            background: rgba(231, 76, 60, 0.2) !important;
            border-color: #e74c3c !important;
            color: #e74c3c !important;
        }
        .restart-btn {
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            color: #050403;
            border: none;
            padding: 14px 28px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 700;
            width: 100%;
            max-width: 220px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="quiz-card" id="quiz-box">
        <div id="portal-content">
            <div class="header">
                <h2>Welcome to Xdzul</h2>
                <div class="subtitle">Select Parameter Setup</div>
            </div>
            <div class="hub-container">
                <div class="hub-btn" onclick="startSelectedQuiz('seismic')">
                    <div class="title">🔐 Seismic Quiz</div>
                    <div class="desc">Privacy-preserving compliance blockchain module.</div>
                </div>
                <div class="hub-btn" onclick="startSelectedQuiz('prismax')">
                    <div class="title">🤖 PrismaX Quiz</div>
                    <div class="desc">Physical AI & data shielded robotic ecosystem.</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let quizzes=[],currentIdx=0,score=0,timeLeft=15,timerInterval=null,canClick=true,isTabActive=true;
        let activeType = '';
        const audioCtx=new(window.AudioContext||window.webkitAudioContext)();

        function playRobotSound(type) {
            try {
                let osc=audioCtx.createOscillator();
                let gain=audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                if(type==='correct') {
                    osc.type='triangle'; osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); 
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1); 
                    gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.2);
                } else if(type==='wrong') {
                    osc.type='sawtooth'; osc.frequency.setValueAtTime(130, audioCtx.currentTime); 
                    osc.frequency.linearRampToValueAtTime(60, audioCtx.currentTime + 0.3); 
                    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.3);
                }
            } catch(e){}
        }

        async function startSelectedQuiz(type) {
            activeType = type;
            let displayTitle = type === 'seismic' ? 'Seismic Systems' : 'PrismaX';
            let displaySubtitle = type === 'seismic' ? '🔒 COMPLIANCE ACTIVE' : '🔒 PHYSICAL AI & DATA SHIELDED QUIZ';
            
            document.getElementById("quiz-box").innerHTML = `
                <div class="header">
                    <h2>\${displayTitle}</h2>
                    <div class="subtitle">\${displaySubtitle}</div>
                </div>
                <div id="quiz-body">
                    <div class="timer-bar-container"><div class="timer-bar" id="t-bar"></div></div>
                    <div class="question" id="q-text">Initializing parameters...</div>
                    <div class="options-container" id="options-box"></div>
                </div>`;
                
            try{
                let e=await fetch(`/get-quiz/\${type}`),t=await e.json();
                quizzes=t.quizzes,currentIdx=0,score=0,showQuestion()
            }catch(e){
                document.getElementById("q-text").innerText="Failed to load parameters."
            }
        }

        function startTimer(){
            clearInterval(timerInterval);
            timeLeft=15; canClick=true; updateTimerBar();
            timerInterval=setInterval(()=>{
                if(!isTabActive) return;
                timeLeft--; updateTimerBar();
                if(timeLeft<=0){ clearInterval(timerInterval); canClick=false; autoTimeOut() }
            },1000)
        }
        function updateTimerBar(){
            let el = document.getElementById("t-bar");
            if(el) el.style.width=(timeLeft/15)*100+"%";
        }
        function showQuestion(){
            if(currentIdx>=quizzes.length){ showResult(); return }
            startTimer();
            let e=quizzes[currentIdx];
            document.getElementById("q-text").innerText=`Parameter \${currentIdx+1} / \th\${quizzes.length}: \${e.question}`;
            let t=document.getElementById("options-box");
            t.innerHTML="",e.options.forEach(n=>{
                let o=document.createElement("button");
                o.className="option-btn",o.innerText=n,o.onclick=()=>checkAnswer(o,n,e.answer),t.appendChild(o)
            })
        }
        function checkAnswer(e,t,n){
            if(!canClick)return;
            clearInterval(timerInterval); canClick=false;
            let o=document.querySelectorAll(".option-btn");
            o.forEach(e=>e.disabled=!0);
            if(t===n){ e.classList.add("correct"); playRobotSound('correct'); score++ }
            else { e.classList.add("wrong"); playRobotSound('wrong'); o.forEach(e=>{if(e.innerText===n)e.classList.add("correct")}) }
            setTimeout(()=>{currentIdx++,showQuestion()},1400)
        }
        function autoTimeOut(){
            playRobotSound('wrong');
            let e=quizzes[currentIdx].answer;
            document.querySelectorAll(".option-btn").forEach(t=>{
                t.disabled=!0;
                if(t.innerText===e)t.classList.add("correct"); else t.classList.add("wrong");
            });
            setTimeout(()=>{currentIdx++,showQuestion()},1400)
        }
        function showResult(){
            clearInterval(timerInterval);
            document.getElementById("quiz-body").innerHTML=`
                <div style="text-align:center;">
                    <h3 style='color:rgb(237, 228, 213);'>Verification Complete</h3>
                    <p style="font-size:24px; color:rgb(237, 228, 213); font-weight:800; margin: 15px 0;">Score: \${score} / \${quizzes.length}</p>
                    <button class="restart-btn" onclick="location.reload()">Back to Hub</button>
                </div>`
        }

        document.addEventListener("visibilitychange", () => {
            isTabActive = !document.hidden;
        });
    </script>
</body>
</html>"""
    return html_content
