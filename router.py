mode="normal"
mode_options = {"pentest","research","crypto"}
def handle_command(prompt,conversation):
    global mode

    parts = prompt.split()
    if prompt.startswith("/mode"):
        if len(parts) < 2:
            print("Usage : /mode normal")
        mode = parts[1]
        print(f"Switched to Mode {mode}")

        if mode not in mode_options:
            print(f"❌ Invalid mode '{mode}'.")
            print(f"✅ Available modes: {', '.join(ALLOWED_MODES)}")
        return True

    if prompt.lower=="/reset":
        conversation[:]=[conversation[0]]
        save_memory(conversation)
        print("Conversation memory reset")
        return True

    if prompt.lower=="/help":
        print("\nexit = End conversation\n/reset = Clear conversation memory\n/help = Show commands")
        return True

    return False
