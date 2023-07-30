import gethistorychatlog
import json

historyChatlog = gethistorychatlog.historyChatlog()
userText = "為什麼會下雨？"


def genPrompt(tracelog: historyChatlog, userText: str):
    prompt = {
        "role": "user",
        "content": userText,
    }
    tracelog.append(prompt)
    jsonTracelog = json.dumps(tracelog, indent=2, ensure_ascii=False)
    print(jsonTracelog)
    return tracelog


genPrompt(historyChatlog, userText)
