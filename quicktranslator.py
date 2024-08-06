import pyperclip
import pyautogui
import aiohttp
import asyncio
import keyboard

config = {
    'delay_after_copying': 0.1,
    'show_errors': True,
    'hotkeys': {
        'f2': 'en',
    }
}

async def translate_text(text, target_language):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": target_language,
        "dt": "t",
        "q": text
    }
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                result = await response.json()
                return ''.join(sentence[0] for sentence in result[0] if sentence[0])
        except aiohttp.ClientError as e:
            if config['show_errors']:
                print(f"Translation error: {e}")
            return None

async def on_hotkey(target_language):
    try:
        pyautogui.hotkey('ctrl', 'c')
        await asyncio.sleep(config['delay_after_copying'])
        
        original_text = pyperclip.paste()
        if not original_text:
            return
        
        translated_text = await translate_text(original_text, target_language)
        if translated_text:
            pyperclip.copy(translated_text)
            pyautogui.hotkey('ctrl', 'v')
    
    except Exception as e:
        if config['show_errors']:
            print(f"An error occurred: {e}")

# Set up hotkeys
for hotkey, language in config['hotkeys'].items():
    keyboard.add_hotkey(hotkey, lambda lang=language: asyncio.run(on_hotkey(lang)))

asyncio.run(asyncio.Event().wait())