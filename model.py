
def predict_emoji(text):
    # Dummy example just for demo
    if "love" in text.lower():
        return "❤️"
    elif "happy" in text.lower():
        return "😄"
    elif "sad" in text.lower():
        return "😞"
    elif "food" in text.lower() or "eat" in text.lower():
        return "🍴"
    elif "game" in text.lower() or "sport" in text.lower():
        return "⚾"
    else:
        return "🤖"
