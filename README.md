<div align="center">

<h1>LinkedIn Automation</h1>
<em>Automation • AI • Scheduler • Web Dashboard</em>

<p>
  <a href="https://github.com/KumarKhailendra/LinkedIn-post-automation/actions/workflows/ci.yml">
    <img alt="CI" src="https://github.com/KumarKhailendra/LinkedIn-post-automation/actions/workflows/ci.yml/badge.svg" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=flat-square" />
  <img src="https://img.shields.io/badge/OpenAI-API-412991?style=flat-square" />
  <img src="https://img.shields.io/badge/LinkedIn-REST_API-0077B5?style=flat-square" />
  <img src="https://img.shields.io/badge/Scheduler-APScheduler-orange?style=flat-square" />
</p>

<!-- Subtle animated typing line (no repo assets required) -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1400&color=7C77C6&center=true&vCenter=true&width=880&lines=Automate+your+LinkedIn+growth;Generate+professional+posts+with+AI;Create+images+via+DALL-E+3;Schedule+from+CLI+or+Web+Dashboard" alt="Typing Animation" />

<p>
  <a href="https://www.linkedin.com/in/KumarKhailendra/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.youtube.com/@buildandlearntime">
    <img alt="YouTube" src="https://img.shields.io/badge/YouTube-Subscribe-FF0000?logo=youtube&logoColor=white" />
  </a>
</p>

</div>

---

## 🚀 What Is This?
A complete LinkedIn automation toolkit:
- 🤖 `ContentGenerator` uses OpenAI Chat + optional DALL‑E 3 image generation
- 🏷️ Smart hashtag generation + graceful fallbacks
- 🖼️ Auto image download & local asset management
- 🔗 Robust `LinkedInPoster` with Posts API + UGC fallback logic
- 🕒 Two scheduling modes:
  - CLI custom scheduling (`schedule_post.py` / `custom_scheduler.py`)
  - Live Django dashboard with animated UI and REST helpers
- 🔄 Background reload of newly added posts (file‑based queue + dynamic job injection)
- 🗃 History tracking: scheduled / completed / failed / expired
- ✨ Web UI: particle background, live clock, quick buttons (Now / +1h / Tomorrow / Next Week)


## Demo 

## 1. 
<img width="1142" height="851" alt="1" src="https://github.com/user-attachments/assets/feb82dab-6800-4b1f-8f89-2b4ab643c465" />


## 2.
<img width="1111" height="882" alt="2" src="https://github.com/user-attachments/assets/2854d808-a828-4d03-838e-4fc04a054591" />



## 🧠 Core Architecture
```
main.py ──► selects mode (test | post-now | schedule)
           │
           ├─► ContentGenerator (OpenAI text + optional image)
           │        └─ fallback content / hashtag strategies
           │
           ├─► LinkedInPoster (Posts API → fallback to UGC)
           │        └─ multi-step image upload register + PUT binary
           │
           └─► CustomPostScheduler (APScheduler BackgroundScheduler)
                    ├─ JSON persistence (scheduled_posts.json)
                    ├─ Auto reload loop (mtime watching)
                    ├─ Status transitions: scheduled → completed/failed/expired
                    └─ Web dashboard integrates via direct file + subprocess
```

## 📂 Project Layout (simplified)
```
/README.md
/.env                      # Your secrets (NOT committed)
/config.json               # Content + image config
/main.py                   # Entry CLI interface
/content_generator.py      # AI text + image logic
/linkedin_poster.py        # Posts / UGC API posting
/custom_scheduler.py       # Background scheduler + persistence
/schedule_post.py          # Rich CLI for add/list/start/cancel
/scheduled_posts.json      # Queue + history (auto-created)
/linkedin_Scheduler/       # Django project
  /posts/                  # Web dashboard app
    templates/home.html    # Animated UI
    static/base.css        # Particle + neon styling
```

## 🔐 Environment Variables (.env)
Create `.env` in project root:
```
OPENAI_API_KEY=sk-...
LINKEDIN_ACCESS_TOKEN=your_linkedin_oauth_token
LINKEDIN_USER_ID=your_numeric_or_profile_id
LINKEDIN_PERSON_URN=urn:li:person:XXXXXXXX   # optional override
```
If `LINKEDIN_PERSON_URN` omitted, it auto-builds from `LINKEDIN_USER_ID`.

## 🛠 Installation
```powershell
# Clone (replace YOUR_REPO)
git clone https://github.com/KumarKhailendra/LinkedIn-post-automation.git
cd LinkedIn-post-automation

# Create virtual env (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Create .env
notepad .env
```

## ⚙️ Config (`config.json`)
Tune topics, length, hashtags, and image settings.
```json
{
  "content_topics": ["AI and Machine Learning", "Software Development Best Practices"],
  "post_length": "medium",
  "include_hashtags": true,
  "max_hashtags": 5,
  "include_images": true,
  "image_size": "1024x1024",
  "image_quality": "standard"
}
```

## 🖥 CLI Usage
```powershell
# 1. Test environment & sample generation
python main.py --mode test --topic "AI and Machine Learning" --with-image

# 2. Post immediately
python main.py --mode post-now --topic "Career Growth Tips" --no-image

# 3. Schedule via quick helper
python main.py --mode schedule --topic "Industry Insights" --time "14:30" --with-image

# 4. Advanced scheduler commands
python schedule_post.py add --topic "Tech News" --time "2025-11-11 09:00"
python schedule_post.py list
python schedule_post.py start
python schedule_post.py cancel --id JOB_ID
python schedule_post.py quick --topic "AI Trends" --when in-1h
```

## 🌐 Web Dashboard (Django)
```powershell
# Run dev server
cd linkedin_Scheduler
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Open: http://localhost:8000
Features:
- Live stats (Scheduled / Completed / Failed)
- Animated particle UI + realtime clock
- Quick schedule buttons
- Modal listing with edit / delete / reschedule actions
- Resilient multi-path scheduling (direct scheduler → subprocess → JSON fallback)

## 🖼 Image Generation Flow
1. Build professional prompt based on topic + config
2. Call DALL‑E 3 (size & quality from `config.json`)
3. Download PNG to `generated_images/` with sanitized filename
4. Attach media URN to post payload (Posts API) or fallback to UGC

## 🔄 Scheduler Mechanics
- Background loop every 30s checks `scheduled_posts.json` mtime
- Adds new posts dynamically without restart
- Marks past scheduled entries as `expired`
- Persists status transitions with timestamps

## 🛡 Error Handling & Fallbacks
| Layer | Primary | Fallback |
|-------|---------|----------|
| Text Generation | OpenAI Chat | Static template |
| Hashtags | AI prompt | Topic-based static list |
| Post API | Posts REST | UGC endpoint |
| Scheduling | APScheduler job | Direct JSON append |

## 📦 Dependencies (minimal)
See `requirements.txt` – generated from imports.

## ✅ Quality Gates
| Gate | Status |
|------|--------|
| Syntax (import compile) | PASS (core scripts parsed) |
| Django start (requires env) | Pending user secrets |
| External APIs | Requires valid tokens |

## 🛠 requirements.txt (generated)
```
openai
python-dotenv
requests
APScheduler
psutil
Django>=5.2,<6.0
```
(Optional extras: `black`, `flake8`, `mypy` for dev.)

## 🙈 .gitignore Essentials
```
# Python
__pycache__/
*.py[cod]
*.sqlite3
.venv/
.env
*.log

# Images
/generated_images/

# Django
staticfiles/
media/

# OS / Editors
*.DS_Store
.vscode/
```
(Actual file added in repo.)

## 🔧 GitHub Setup
```powershell
git init
git add .
git commit -m "feat: initial LinkedIn automation toolkit"
git branch -M main
git remote add origin https://github.com/KumarKhailendra/LinkedIn-post-automation.git
git push -u origin main
```

## 🎬 Suggested Demo Assets
Create and add:
- `assets/banner.gif` – animated gradient title
- `assets/cli-demo.gif` – recording of scheduling & posting
- `assets/dashboard.gif` – short screen capture of Django UI
Update the banner URL near top once pushed.

## 🔒 Disclaimer
Use responsibly. Comply with LinkedIn Platform Terms. Excessive automation may violate TOS. Add human review for critical posts.

## 📈 Future Enhancements
- OAuth refresh flow & token auto-renew
- Retry queue for failed posts
- Redis / Postgres backend
- Rich analytics (engagement, impressions, CTR)
- WebSocket real-time updates

## ❤️ Contributing
PRs welcome. Open an issue for bugs or feature ideas.

## 🤝 Connect & Support
- Connect: <a href="https://www.linkedin.com/in/khailendra-prasad/">LinkedIn @khailendra-prasad</a>
- Subscribe: <a href="https://www.youtube.com/@buildandlearntime">YouTube @buildandlearntime</a>
- If this helped, ⭐ star the repo and share!

---
<div align="center">
Made with 💡, ⚙️ & ☕ — Automate your professional presence.
<br/>
<a href="https://www.linkedin.com/in/khailendra-prasad/">LinkedIn</a> • <a href="https://www.youtube.com/@buildandlearntime">YouTube</a>
</div>
