# <img src="https://i.ibb.co/bJtL1KV/52f6be4a-16d2-4f31-8e90-b8cd20670810-removebg.png" width="28px" /> DrugGeneExplorer

<div align="center">
  <img width="200" src="https://i.ibb.co/bJtL1KV/52f6be4a-16d2-4f31-8e90-b8cd20670810-removebg.png">
</div>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg" />
  </a>
  <a href="https://www.python.org/">
    <img
      alt="Python Version"
      src="https://img.shields.io/badge/Python-%3E=3.9,%3C=3.12-red"
    />
  </a>
  <a href="https://github.com/BerriAI/litellm">
    <img
      alt="litellm"
      src="https://img.shields.io/badge/%20%F0%9F%9A%85%20liteLLM-OpenAI%7CBing%7CSydney%7CDGBDI-blue?color=blue"
    />
  </a>
</p>

> [!NOTE]
> A special thanks to **[vsakkas](https://github.com/vsakkas/sydney.py/)** for creating the Sydney-py library, and to all those who contributed to its inception and upkeep.


> A DrugGeneExplorer robot based on Coopilot with no risk, very stable! 🚀

## 🎤 Introduction

> This Python bot is designed to gather interactions data from the Drug-Gene Interaction Database (`DGIdb`) and utilizes the `sydney-py` library to obtain more detailed information about specific interactions.

## 🌟 Features

- [x] **Interactive User Interface:**
  - Welcomes the user and prompts for input.
  - Asks for the names of three drugs.
  - Allows the user to choose whether to get additional information on a specific gene.
  - Enables the user to continue making requests or exit the program.

- [x] **Drug-Gene Interaction Retrieval:**
  - Utilizes the DGIdb API to fetch interactions for the specified drugs.
  - Processes the retrieved data to extract relevant information.

- [x] **Detailed Information with "sydney-py":**
  - Uses the "sydney-py" library to obtain detailed information about a selected gene.
  - Presents the user with options to explore additional details about a gene based on the interaction results.

- [x] **Error Handling:**
  - Handles connection errors gracefully, providing informative messages.
  - Catches various exceptions during the API request process and displays appropriate error messages.

- [x] **Rich Console Output:**
  - Utilizes the "rich" library for visually appealing console output.
  - Presents information in a structured and easy-to-read format using panels.

- [x] **Asynchronous Execution:**
  - Uses asynchronous programming with `asyncio.run(main())` for efficient handling of user interactions and API requests.

- [x] **Code Modularity:**
  - Organizes code into functions for improved readability and maintainability.
  - Separates concerns for handling user input, making API requests, processing data, and interacting with "sydney-py."

- [x] **Dependencies:**
  - Lists necessary dependencies (requests, sydney, rich) for users to install before running the script.

- [x] **Informative Welcome Message:**
  - Displays a friendly welcome message with emojis to create a positive user experience.

- [x] **Documentation:**
  - Includes inline comments explaining the purpose of functions and sections of the code.
  - Offers a clear structure for easy understanding of the code logic.


## 🚀 Getting Start

> It is recommended that the Python version be between 3.9.X~3.10.X, version 3.10-3.11 is perfect

#### 1. Clone repo

```bash
https://github.com/BlackDicky/DrugGeneExplorer.git
```

## Dependencies
- requests
- io
- asyncio
- sydney
- rich

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### Start Script

- **Once all the steps are completed, you can launch the script by using the command `python3 DrugGeneExplorer.py`**
