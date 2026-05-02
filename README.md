VineAI Android Agent 🤖📱

VineAI is a modular AI agent built entirely on an Android device with $0 budget using Termux — no laptop, no cloud server, and no paid infrastructure required.

It demonstrates how far you can push mobile development using Python,API-driven AI,clean system design and absolute stubbornness to build even with various constraints ✌️

---

🚀 Key Features

- 🧠 AI-Powered Conversations
  Uses open source AI models like zhipu AI GLM to generate intelligent responses.

- 🧩 Modular Architecture
  Clean separation of concerns:
  
  - "router.py" → command handling layer
  - "api.py" → model communication
  - "memory.py" → persistence system
  - "config.py" → centralized configuration

- ⚡ Command Routing System
  Supports local commands (e.g. reset, exit, etc.) that bypass the AI model for speed and control.

- 💾 Persistent Memory
  Conversation history is saved and reloaded across sessions.

- 🧹 Text Normalization Layer
  Ensures consistent formatting and avoids encoding issues.

- 📱 Fully Mobile Development
  Built and run entirely inside Termux on Android.

---

🏗️ Project Structure

VineAI/
│
├── main.py        # CLI loop + core execution flow
├── router.py      # Command handling logic
├── api.py         # AI model interaction
├── memory.py      # Load/save conversation memory
├── config.py      # System settings and constants
└── README.md

---

🧠 How It Works

1. User enters input in the CLI
2. Input is passed to the command router
   - If it's a command → handled locally
   - If not → sent to the AI model
3. Response is added to conversation memory
4. Memory is trimmed to stay within limits

This creates a hybrid system:

- ⚙️ Deterministic command execution
- 🤖 Probabilistic AI responses

---

⚙️ Setup (Termux)

pkg update && pkg upgrade
pkg install python git

git clone https://github.com/YOUR_USERNAME/VineAI-android-agent-.git
cd VineAI-android-agent-

pip install -r requirements.txt
python main.py

---

🔑 Configuration

Edit "config.py" to set:

- API keys
- system prompt
- max conversation length

---

💡 Why This Project Matters

This project shows that:

- You don’t need expensive hardware to build AI systems
- Mobile devices can run structured, modular AI agents
- Clean architecture matters even in small projects

---

🔮 Future Improvements

- Tool/plugin system (like function calling)
- Web interface or local dashboard
- Streaming responses
- Multi-agent coordination
- Voice input/output

---

📜 License

MIT License

---

👤 Author

Built by a Tech & innovation lover pushing the limits of mobile-based AI engineering and global Fintech solutions.