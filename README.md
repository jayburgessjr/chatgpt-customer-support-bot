# ChatGPT-Powered Customer Support Bot

## Description
This project demonstrates how to create a customer support chatbot powered by OpenAI’s GPT API. The chatbot can handle common queries, provide helpful responses, and escalate unresolved issues to human agents when needed.

## Features
- Answer frequently asked questions (FAQs).
- Perform sentiment analysis to assess customer satisfaction.
- Escalate complex issues to human agents.
- Log chat history for performance analysis and training.
- Provide multi-language support for international users.
- Allow administrators to update FAQs dynamically.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chatgpt-customer-support-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chatgpt-customer-support-bot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the chatbot:
   - Update the `chatbot_config.json` with FAQs and bot settings.
   - Add your OpenAI API key in the `.env` file.

5. Run the chatbot:
   ```bash
   python main.py
   ```

## Files
1. `main.py`: Backend script for handling chatbot logic.
2. `requirements.txt`: Dependencies for the project.
3. `chatbot_config.json`: Configuration file for intents and FAQs.
4. `sample_responses.json`: Mock dataset of customer FAQs and responses.
5. `chat_logger.py`: Script for logging chat history.

## Example Use Case
- A customer asks: "What is your refund policy?"
- The chatbot replies with: "Our refund policy allows you to return items within 30 days of purchase."
