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

&ensp;[<kbd> <br> Introduction <br> </kbd>](#Introduction)&ensp;
&ensp;[<kbd> <br> Features <br> </kbd>](#Features)&ensp;
&ensp;[<kbd> <br> Getting Start <br> </kbd>](#Getting-Start)&ensp;
&ensp;[<kbd> <br> Dependencies <br> </kbd>](#Dependencies)&ensp;

## <img src="https://i.ibb.co/nRxHpxT/medicine.png" width="45px" /> Introduction

> This Python bot is designed to gather interactions data from the Drug-Gene Interaction Database (`DGIdb`) and utilizes the `sydney-py` library to obtain more detailed information about specific interactions.


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


- **Once all the steps are completed, you can launch the script by using the command `python3 DrugGeneExplorer.py`**

> [!IMPORTANT]
> `In progress of finalizing everything; it should be ready within a few days.`
