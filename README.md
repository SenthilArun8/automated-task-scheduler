# 🕒 Automated Task Scheduler

A lightweight Python script that automates the execution of batch (`.bat`) files at scheduled times. This is a classic example of **automation**: predefined tasks triggered by precise rules — no surprises, just execution.

> “Automation. This is basically the simplest form of ‘getting stuff done automatically.’ It’s when a program follows a set of rules and does predefined tasks… It’s reliable, quick, and pretty straightforward…”  
> — [u/OptionalChalk on r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1hqzzrg/if_youre_unsure_what_agentic_ai_is_and_whats_the/)

---

## 🔧 Features

- 🗂️ **Read from config:** Centralized settings using a `config.json` file
- 🕘 **Flexible scheduling:** Set batch files to run at specific times using a human-readable format
- 🔁 **Daily repetition:** Auto-reschedules tasks for the next day
- 📄 **Task management:** Easy task input using a plain `.txt` file
- 🧪 **Simple logging:** Console output for monitoring execution and errors

---

## 📁 File Structure

```bash
.
├── config.json           # Settings (task file path, delimiter)
├── tasks.txt             # List of scheduled tasks
├── automated_task_runner.py  # Main script
