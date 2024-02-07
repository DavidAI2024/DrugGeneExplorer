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

> [!TIP]
> - `citations`: if set to `True`, the AI's response will include **links** to the sources from which it has extracted information. If set to `False`, the AI's response will not show citations. The default value is `False`.
>
> - `search`: if set to `True`, the AI will seek the answer through the **internet**, using Bing as the search engine. If set to `False`, the AI will only utilize its computational power, relying on its internal knowledge. The default value is `False`.


## <img src="https://i.ibb.co/LPp8y3N/genes.png" width="45px" /> Features

- [x] **Interaction with Sydney**
  - Utilizes the Sydney module to acquire detailed and contextually informative responses concerning drug-gene interactions.

- [x] **Command-Line Interface (CLI)**
  - Offers an intuitive command-line interface, facilitating seamless interaction with scripts.

- [x] **Graphical Gene Interactions Chart**
  - Generates a bar chart illustrating gene interactions related to a user-selected gene, providing a visual representation of information.

- [x] **Elegant Response in PyQt5 Box**
  - Displays responses in a graphical box created with PyQt5, offering a visually pleasing and user-friendly experience.

- [x] **Customizable Font:**
  - Users can enhance personalization by changing the font. Simply install the preferred font locally and specify the TTF file path.

- [x] **Rich Box Visualization**
  - Presents drug-gene interactions in visually formatted Rich boxes for enhanced clarity.

- [x] **Interaction Details**
  - Exhibits crucial interaction details, including scores, interaction types, gene names, and more.

- [x] **Minimum Requirements**
  - Requires Python 3.9 - 3.11 as the execution environment.
  - External dependencies, such as rich, Sydney, PyQt5, requests, and matplotlib, can be effortlessly installed with the command `pip install -r requirements.txt`.

- [x] **Simple Usage Instructions**
  - Follow the provided instructions to install dependencies and run the script, ensuring a straightforward and immediate application usage.

- [x] **Author Information**
  - Includes a dedicated section for project authors.

- [x] **Open Source License (MIT)**
  - Distributed under the MIT license, ensuring transparent and clear management of usage conditions.

- [x] **Reset Conversation Command**
  - Introduces a new feature: users can reset the conversation with the AI using the command "!reset."





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


## <img src="https://i.ibb.co/ZWQFnLS/pills-bottle.png" width="45px" /> Dynamic Visualization of the Tool in Action

| Start |
| :-: |
| ![Start](https://i.ibb.co/3dRyQ1t/Screenshot-2024-02-05-15-58-08-1920x1080.png) |

| Drug-gene interaction research |
| :-: |
| ![Drug-Gene](https://i.ibb.co/jHd2Q8y/Screenshot-2024-02-05-15-58-28-1920x1080.png) |

| Interaction results |
| :-: |
| ![Interactions](https://i.ibb.co/t4tykrC/Screenshot-2024-02-05-15-58-38-1920x1080.png) |

| Graph of all genes interacting with the selected drug, highlighting the one with the most significant interference among them all. |
| :-: |
| ![Genes](https://i.ibb.co/GFjntRJ/Screenshot-2024-02-05-15-58-47-1920x1080.png) |

| Selection of the gene to be passed to artificial intelligence for a detailed analysis of the interaction between the drug and the gene. |
| :-: |
| ![Image#1](https://i.ibb.co/Js8CR1x/Screenshot-2024-02-05-15-59-02-1920x1080.png) |
| ![Image#2](https://i.ibb.co/qCdcCMC/Screenshot-2024-02-05-15-59-08-1920x1080.png) |

| Final Response in both CLI (Command Line Interface) and GUI (Graphical User Interface) Formats. |
| :-: |
| ![FinalResponse](https://i.ibb.co/MgT6fsF/Screenshot-2024-02-05-16-01-57-1920x1080.png) |
