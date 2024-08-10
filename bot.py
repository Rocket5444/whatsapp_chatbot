import pyautogui
import time
import pyperclip
import os
from openai import OpenAI

# Store your API key in an environment variable
os.environ["OPENAI_API_KEY"] = "<api_key>"

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def is_last_message_from_sender(chat_log, sender_name="Anushka"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024")[-1]
    if sender_name in messages:
        return True
    return False

# Step 1: Click on the icon coordinates (1434, 1049)
pyautogui.click(1434, 1049) 
time.sleep(1) # Wait for 1 sec to ensure the click is registered

while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (739, 132) to (1842, 922) to select the text
    pyautogui.moveTo(736, 126)
    pyautogui.dragTo(736, 948, duration=2.0, button='left') # Drag for 2 sec

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(666, 161)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    if is_last_message_from_sender(chat_history):
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a person named Kunal who speaks Marathi as well as English. You are from India and you are a coder. You analyze chat history and respond like Kunal."},
                    {"role": "system", "content": "Do not start like this [11:57 pm, 8/8/2024] Anushka:"},
                    {"role": "user", "content": chat_history}
                ]
            )
            response = completion.choices[0].message.content
            pyperclip.copy(response)

            # Step 5: Click at coordinates (825, 980)
            pyautogui.click(825, 980)
            time.sleep(1)

            # Step 6: Paste the text
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

            # Step 7: Press Enter
            pyautogui.press('enter')
        except Exception as e:
            print(f"Error: {e}")
