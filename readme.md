# AI Agent from Scratch

![Sample](/sample.png)

This project is a simple yet powerful implementation of an AI agent built from scratch using Hugging Face's `InferenceClient` and integrating basic tools like a calculator. The agent is capable of interacting with users, performing arithmetic operations, and responding intelligently based on the context.

## Features

- **AI Agent**: A custom AI agent built with Hugging Face's models that can interact with users, interpret queries, and provide responses.
- **Tool Integration**: A built-in calculator tool to perform arithmetic operations like addition, subtraction, multiplication, division, and more.
- **Verbose Logging**: Logs are maintained for every agent interaction, providing insights into internal processes such as tool usage and thoughts.
- **Streamlit Interface**: A web-based user interface built with Streamlit for interacting with the agent and viewing verbose logs.

## Installation

### Prerequisites

- Python 3.11 or higher
- Poetry for managing dependencies and environments (or use `pip` if you prefer)

### Step-by-step Installation

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd ai-agent-from-scratch
    ```
2. **Install Dependencies using Poetry**

   If you don't have Poetry installed, follow the instructions on [Poetry's website](https://python-poetry.org/docs/#installation) to install it.

   Then, install the project dependencies:
   ```bash 
   poetry install
   ```


3. **Setup Environment Variables**

   Create a `.env` file in the root directory and add your Hugging Face API token as follows:

   hf_api=YOUR_HUGGING_FACE_API_TOKEN

4. **Run the Application**

   Once the dependencies are installed and the environment is set up, you can run the Streamlit app:
    ```bash
   streamlit run app.py
    ```
   This will start the application locally, and you can access it via your browser at `http://localhost:8501`.

## How It Works

1. **Agent Initialization**: The agent is initialized with the Hugging Face API token and available tools like the calculator. The model used for the agent is `microsoft/Phi-3.5-mini-instruct`.
2. **User Interaction**: The user types a query into the input field, and the agent decides whether to provide a direct response or use a tool.
3. **Tool Usage**: If the query requires an external tool, like the calculator, the agent generates the appropriate tool action and invokes it.
4. **Verbose Logs**: Every interaction with the agent, including tool usage and thought processes, is logged and displayed in the right column of the UI for transparency.

## Example Queries

- **Basic Chat**: "How are you?"
- **Math Operations**: "What is 125 times 165?"
- **Geometric Calculations**: "What is the area of a square with side length of 16.25?"

## Code Overview

### `app.py`
This file contains the Streamlit frontend that handles the UI and user interaction with the agent. It provides an interface for both the user and the verbose logs.

### `agent.py`
This file contains the `Agent` class that handles the logic of interacting with the Hugging Face API, using tools, and maintaining the chat history.

### `tools.py`
This file defines the available tools for the agent, like the calculator. The calculator performs basic arithmetic operations based on user input.

### `prompts.py`
Defines the prompts used to guide the agent in various scenarios. It includes the system prompt, tool instructions, and general guidelines.

### `test.py`
A script to test the functionality of the agent with sample queries. Useful for validating the agent's responses and tool usage.

### `pyproject.toml`
Configuration for managing dependencies, versioning, and project setup using Poetry.

## Dependencies

The project relies on the following Python libraries:

- **huggingface-hub**: For interacting with Hugging Face models.
- **ipykernel**: For running Jupyter kernels.
- **python-dotenv**: For managing environment variables.
- **streamlit**: For building the web interface.

## Troubleshooting

If you encounter any issues:

- Ensure that your Hugging Face API token is valid.
- Check if the environment variables are correctly set in the `.env` file.
- Make sure all dependencies are installed using `poetry install` or `pip install`.

## License

This project is open-source and available under the [MIT License](LICENSE).
