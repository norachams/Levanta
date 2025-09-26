# Levanta 🚀

Levanta is a tough-love motivational SMS bot that pushes you to stay consistent with your daily LeetCode grind.  
Every day at 12 PM, it sends you a sarcastic, FOMO-inducing motivational text *plus* a random unsolved LeetCode problem to work on.  
No excuses. No mercy. Just accountability.

---

## ✨ Features
- **Daily SMS reminders** at a fixed time using GitHub Actions (cron jobs).
- **Brutal motivational messages** generated with Cohere’s `command-a-03-2025` model.
- **Unique real-life examples** (e.g., Clément Mihailescu, Marie Curie, Thomas Edison) — never repetitive.
- **Dynamic problem assignment**: pulls unsolved problems from your GitHub LeetCode repo and assigns one each day.
- **Twilio integration**: sends reminders straight to your phone.
- **History tracking**: remembers past messages to avoid repeats.

---

## ⚙️ How It Works
1. **GitHub Actions** runs the bot daily at the scheduled time.
2. **Cohere API** generates a motivational message with tough-love style.
3. **GitHub API** checks your solved LeetCode problems, compares with your full problem set, and picks a random unsolved one.
4. **Twilio API** sends the combined message + problem directly to your phone.
5. **Supabase** to store old messages and avoid repetitions in messages.

---

## 🛠️ Tech Stack
- **Python 3.12**
- **Cohere API** (AI-generated motivational texts)
- **GitHub API** (track solved problems from your repo)
- **Twilio API** (send SMS)
- **GitHub Actions** (daily automation)
- **Supabase** (saves old messages in db)
- **SpaCy NER** (to extract names and avoid exmaple repetitions"

---

## 🚀 Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Levanta.git
   cd Levanta
   ```

2. Create a .env file with your keys:

    ```bash
    MY_GITHUB_TOKEN=your_github_token
    COHERE_TOKEN=your_cohere_token
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_TOKEN=your_twilio_token
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   python Main.py
   ```

---

## ⚡ Deployment with GitHub Actions

The workflow file `.github/workflows/levanta.yml` is already configured.
It:
- Installs dependencies
- Runs `Main.py`
- Sends your motivational SMS automatically

By default, it’s scheduled to run daily at 12 PM Toronto time.

---

## 📱 Example Output

```bash
   You're binge-watching Netflix while J.K. Rowling wrote 'Harry Potter' as a single mom on welfare.
   She didn't wait for a fairy godmother, she wrote every damn day.
   'Discipline is the bridge between goals and accomplishment.'
   Your bridge is collapsing. Open LeetCode. Now. Solve one problem today.

    Today's problem: Champagne Tower
   ```

---
## 🔑 Notes 

- Twilio trial accounts only allow sending SMS to verified numbers.
- Keep messages under 320 characters (46 words) for best deliverability (longer messages split into segments).
- The name Levanta comes from Spanish: “Rise up.”

