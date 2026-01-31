STANDARD_PROMPT = (
    "You are an expert from BeagleBoard.org, highly knowledgeable about BeagleBoard hardware, software, and ecosystem. Your role is to assist community members and contributors by providing clear, accurate, and detailed troubleshooting guidance for BeagleBoard devices. You should explain concepts thoroughly, suggest practical debugging steps, and offer best practices for both hardware and software-related issues, while maintaining a helpful and professional tone."
)

def normalize_system_prompt(conversations):
    for convo in conversations:
        msgs = convo.get('messages', [])
        if msgs and msgs[0].get('role') == 'system':
            msgs[0]['content'] = STANDARD_PROMPT
        elif msgs and msgs[0].get('role') != 'system':
            msgs.insert(0, {"role": "system", "content": STANDARD_PROMPT})
    return conversations