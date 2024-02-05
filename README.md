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


> [!WARNING]
>  <strong><img src="https://i.ibb.co/Kjm2rfS/alert.png" width="28px" />
Alpha Version</strong>
> This code is currently in an alpha phase and may contain bugs or instability. I am an evolving novice and learning during the development process. This tool was created in my spare time, fueled by a passion for knowledge and experimentation.
> 
> **Required Changes:**
> Since this is an alpha version, it is likely that changes or optimizations may be necessary to improve the efficiency and stability of the tool. You are encouraged to contribute, suggest improvements, or report issues. Your participation is crucial to make this tool more robust and functional.
> 
> Thanks to everyone who will use this tool and contribute to its evolution. Your collaboration is invaluable for the continuous improvement of the project. <img src="https://i.ibb.co/S06VSzt/thank-you-1.png" width="28px" />



> [!NOTE]
> A special thanks to **[vsakkas](https://github.com/vsakkas/sydney.py/)** for creating the Sydney-py library, and to all those who contributed to its inception and upkeep.



> A DrugGeneExplorer robot based on Coopilot with no risk, very stable! 🚀


## <img src="https://i.ibb.co/nRxHpxT/medicine.png" width="45px" /> Introduction

> This Python bot is designed to gather interactions data from the Drug-Gene Interaction Database (`DGIdb`) and utilizes the `sydney-py` library to obtain more detailed information about specific interactions.

> [!IMPORTANT]
> Before using Sydney.py, it's essential to gather the necessary authentication cookies from the Copilot web page. These cookies will be utilized to authenticate your requests to the Copilot API.

To obtain the cookies, follow these steps using Microsoft Edge:

1. Navigate to the Copilot web page.
2. Open the developer tools in your browser (typically by pressing F12 or right-clicking on the chat dialog and selecting Inspect).
3. Access the Network tab to observe all requests sent to Copilot.
4. Write a message in the chat dialog on the web page.
5. Identify a request named `create?bundleVersion=XYZ` and click on it.
6. Scroll down to the requests headers section and copy the entire value after the `Cookie:` field.

Next, set the obtained value as an environment variable in your shell:

```bash
export BING_COOKIES=<your-cookies>
```
or, in your Python code:

```python 
os.environ["BING_COOKIES"] = "<your-cookies>"
```


## <img src="https://i.ibb.co/LPp8y3N/genes.png" width="45px" /> Features

- [x] **Interaction with Sydney**
  - Utilizes the Sydney module to obtain detailed and contextually informative responses on drug-gene interactions.

- [x] **Command-Line Interface (CLI)**
  - Provides an intuitive command-line interface, facilitating script interaction.

- [x] **Graphical Gene Interactions Chart**
  - Generates a bar chart of gene interactions concerning a user-selected gene, offering a visual representation of information.

- [x] **Elegant Response in PyQt5 Box**
  - Displays responses in a graphical box created with PyQt5, providing a visually pleasing and intuitive user experience.

- [x] **Rich Box Visualization**
  - Presents drug-gene interactions in visually formatted Rich boxes.

- [x] **Interaction Details**
  - Displays important interaction details, including scores, interaction types, gene names, and more.

- [x] **Minimum Requirements**
  - Requires Python 3.9 - 3.11 as the execution environment.
  - External dependencies, including rich, sydney, PyQt5, requests, and matplotlib, can be easily installed with the command `pip install -r requirements.txt`.

- [x] **Simple Usage Instructions**
  - Follow the provided instructions to install dependencies and run the script, making application usage straightforward and immediate.

- [x] **Author Information**
  - Provides a section dedicated to the project authors.

- [x] **Open Source License (MIT)**
  - Distributed under the MIT license to ensure clear and transparent management of usage conditions.

- [x] **Reset Conversation Command**
  - Introducing a new feature, the conversation with the AI can be reset using the command "!reset."




## <img src="https://i.ibb.co/CbsKHRq/start-button.png" width="45px" /> Getting Start

> It is recommended that the Python version be between 3.9.X~3.10.X, version 3.10-3.11 is perfect

#### 1. Clone repo

```bash
https://github.com/BlackDicky/DrugGeneExplorer.git
```

## <img src="https://i.ibb.co/ZG8JF1H/database.png" width="45px" /> Dependencies

Make sure to install the following dependencies before running the project:

- **requests**: HTTP library for making requests.
- **asyncio**: Library for writing asynchronous code using coroutines.
- **sydney**: [SydneyClient](https://github.com/vsakkas/sydney.py) - A library that interfaces with Copilot by Microsoft, leveraging the artificial intelligence of Bing and powered by GPT-4.
- **rich**: Terminal rendering library for rich text and beautiful formatting.
- **matplotlib**: Plotting library for creating visualizations.
- **PyQt5**: Python bindings for the Qt application framework.
- **pandas**: Data manipulation library for working with structured data.
- **kaleido**: Static image export for Plotly charts.

To install the dependencies, you can use the provided `requirements.txt` file. Run the following command:

```bash
pip install -r requirements.txt
```

### <img src="https://i.ibb.co/SdDdstT/gene-therapy.png" width="40px" /> Start Script


- **Once all the steps are completed, you can launch the script by using the command:**
```bash
 python3 DrugGeneExplorer.py
 ```

> [!WARNING]
> **Important Note:**
> <img src="https://i.ibb.co/xh8wChq/party-1.png" width="28px" /> This tool includes the display of emojis to enhance the user experience. Before using the tool, make sure that your terminal supports emoji rendering. Some terminals might not display emojis correctly, which could affect the appearance and understanding of the output.
>
> If your terminal doesn't support emojis, you may encounter unexpected visualizations or unrecognized characters. To avoid this issue, we recommend using a terminal that is compatible with emojis or enabling emoji support in your environment.

> [!TIP]
> **Note for Handling Infinite Loop:**
> 🔄 In the rare event that the tool enters an infinite loop without providing a response, you can interrupt the process by simultaneously pressing `Ctrl + Z` or `Ctrl + C` on your keyboard.
>
> This keyboard shortcut combination will help you terminate the tool's execution and regain control of your terminal. If you experience persistent issues or have any questions, please consider opening an [issue](https://github.com/DavidAI2024/DrugGeneExplorer/issues) in the designated "Issues" section.
>
> Your feedback is valuable to us, and we'll do our best to address and resolve any concerns you may have.


