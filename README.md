# Spelling Helper

A simple Python CLI tool to help practice spelling. The tool reads a word aloud, listens to your spelling, and provides feedback.

## Features

-   **Random Word Selection**: Picks a random word from a customizable list.
-   **Text-to-Speech**: Pronounces the word for you.
-   **Speech-to-Text**: Listens to your voice to check the spelling.
-   **Instant Feedback**: Tells you if you are correct or provides the right spelling if you are wrong.

## Prerequisites

-   Python 3
-   PortAudio (required for PyAudio)
    -   **macOS**: `brew install portaudio`
    -   **Linux**: `sudo apt-get install portaudio19-dev`

## Installation

1.  **Clone the repository** (or navigate to the project directory).

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Make sure your virtual environment is active**:
    ```bash
    source venv/bin/activate
    ```

2.  **Run the tool**:
    ```bash
    python main.py
    ```

3.  **Follow the prompts**:
    -   The tool will say "Please spell the word [word]".
    -   Speak the spelling clearly (e.g., "C A T").
    -   The tool will confirm if you are correct or show the correct spelling.

## Configuration

You can add your own words to the `words.txt` file. Just add one word per line.
