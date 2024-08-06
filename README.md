# Quick Translator

A simple Python script that allows instant translation of copied text using hotkeys.

## Features

- Translate copied text with a single hotkey press
- Automatically pastes the translated text
- Configurable hotkeys and target languages
- Uses Google Translate API

## Requirements

- Python 3.7+
- `pyperclip`
- `pyautogui`
- `aiohttp`
- `keyboard`

## Usage

1. Install the required packages:
   ```
   pip install pyperclip pyautogui aiohttp keyboard
   ```

2. Run the script:
   ```
   python main.py
   ```

3. Use the configured hotkey (default: F2) to translate copied text to the target language.

## Configuration

Edit the `config` dictionary in `main.py` to customize:

- Hotkeys and target languages
- Delay after copying
- Error display

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
