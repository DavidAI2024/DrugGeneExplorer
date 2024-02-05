import os
import requests
import asyncio
from requests.exceptions import ConnectionError, Timeout, RequestException
from sydney import SydneyClient
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import random
import matplotlib.pyplot as plt
import time
from rich.progress import Progress
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt


console = Console()


class NoConnectionException(Exception):
    pass

class ConnectionTimeoutException(Exception):
    pass

class NoResponseException(Exception):
    pass

class ThrottledRequestException(Exception):
    pass

class CaptchaChallengeException(Exception):
    pass

class ConversationLimitException(Exception):
    pass

class CreateConversationException(Exception):
    pass

class GetConversationsException(Exception):
    pass



def format_sydney_response(response_content):
    formatted_content = response_content.replace('**', '<strong>').replace('**', '</strong>')

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @font-face {{
                font-family: 'Recursive';
                src: url('/home/youre_directory/Cormorant_Garamond,Recursive/Recursive/static/Recursive-Regular.ttf');
            }}
            
            body {{
                font-family: 'Recursive', serif;
                font-size: 17px;
                line-height: 1.6;
                margin: 20px;
                background-color: #f0f4f8;
                color: #333;
            }}
            h1 {{
                color: #a7c5eb;
                text-align: center;
                opacity: 0;
                animation: fadeIn 1s ease-in-out forwards;
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                }}
                to {{
                    opacity: 1;
                }}
            }}
            p {{
                margin-bottom: 15px;
            }}
            blockquote {{
                border-left: 4px solid #a7c5eb;
                margin: 15px 0;
                padding-left: 15px;
                color: #555;
            }}
            a {{
                color: #a7c5eb;
                text-decoration: underline;
            }}
            strong {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>DrugGeneExplorer</h1>
        <p>{formatted_content}</p>
    </body>
    </html>
    """







os.environ["BING_COOKIES"] = "YOURE_COOKIE_SYDNEY"

user_data = {}


available_colors = ["red", "yellow", "magenta", "green", "blue"]

async def main() -> None:
    async with SydneyClient(style="creative") as sydney:
        try:
            while True:
                start()

                available_colors = ["blue", "red", "yellow", "magenta", "green"]

                color_input1 = random.choice(available_colors)
                drugs_input = console.input(f"[{color_input1}]Please enter 1 drug or a maximum of 3 drugs in order to analyze gene interactions: ")
                handle_drugs(drugs_input)

                color_input2 = random.choice(available_colors)
                prompt_gene_info = console.input(f"[{color_input2}]Do you want additional information about a specific gene? (Yes/No): ").lower()
                if prompt_gene_info == "yes":
                    color_input4 = random.choice(available_colors)
                    result_number = int(console.input(f"[{color_input4}]Enter the result number for which you want more information: "))
                    selected_gene_name, selected_drug_name = get_selected_gene_and_drug(result_number)
                    await ask_sydney_about_gene(sydney, selected_gene_name, selected_drug_name)

                prompt_reset = console.input(f"Do you want to reset the conversation with Sydney? (Type '!reset' to reset, any other input to continue): ")
                if prompt_reset == "!reset":
                    await sydney.reset_conversation()
                    console.print(Panel.fit("Successfully reset!"))
                    continue

                prompt_continue = input("Do you want to make another request? (Yes/No): ").lower()
                if prompt_continue != "yes":
                    break

        except NoConnectionException:
            handle_exception("No connection to Copilot was found. Please retry.")
        except ConnectionTimeoutException:
            handle_exception("Failed to connect to Copilot, connection timed out. Please retry.")
        except NoResponseException:
            handle_exception("No response was returned from Copilot. Please retry or use a new cookie.")
        except ThrottledRequestException:
            handle_exception("Request is throttled. Please wait and retry.")
        except CaptchaChallengeException:
            handle_exception("Captcha challenge must be solved. Please use a new cookie.")
        except ConversationLimitException:
            handle_exception("Reached conversation limit of N messages. Start a new conversation.")
        except CreateConversationException:
            handle_exception("Failed to create conversation. Please retry or use a new cookie.")
        except GetConversationsException:
            handle_exception("Failed to get conversations. Please retry.")
        except Exception as e:
            handle_exception(e)


def get_selected_gene_and_drug(result_number):
    gene_names = list(user_data["gene_interactions"].keys())
    selected_gene_name = gene_names[result_number - 1]
    selected_drug_name = user_data["gene_interactions"][selected_gene_name]["drugs"][0]
    return selected_gene_name, selected_drug_name



available_colors = ["red", "yellow", "magenta", "green", "blue"]

async def ask_sydney_about_gene(sydney, gene_name, drug_input):
    prompt = (
        f"Information about the interaction between the drug {drug_input} and gene {gene_name} "
        "Provide comprehensive details on how the specified drug "
        f"affects the expression or function of the {gene_name}. Include information on potential side effects, "
        "therapeutic implications, and any relevant research findings. Ensure the response is clear, concise, "
        "and covers the molecular and clinical aspects of the drug-gene interaction."
    )

    os.system("clear")
    panel_color = random.choice(available_colors)
    gene_color = random.choice("yellow")

    console.print(Panel(Align(f"🩺 Wait for the answer on the gene: {gene_name}", style=f"bold {panel_color}", align="center")))

    user_text = """\
        
`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
   `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
     DNA        DNA        DNA        DNA
   ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
        
    """
    console.print(Panel(Align(user_text, style="bold blue", align="center")))

    response_content = ""

    try:
        
        response = await sydney.ask(prompt, citations=False, search=False)
        response_content += response

        
        panel_color = random.choice(available_colors)
        console.print(Panel(response_content, style=f"bold {panel_color}", title="AI-DrugGene"))

        
        formatted_response = format_sydney_response(response_content)
        show_response_popup(formatted_response)

    except Exception as e:
        handle_exception(e)



def show_response_popup(formatted_response):
    app = QApplication([])

    window = QMainWindow()
    window.setWindowTitle("DrugGeneExplorer Response!")

    central_widget = QWidget()
    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setHtml(formatted_response)
    text_edit.setReadOnly(True)
    layout.addWidget(text_edit)

    close_button = QPushButton("Close")
    close_button.clicked.connect(app.quit)
    layout.addWidget(close_button)

    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    window.setGeometry(100, 100, 600, 400)
    window.show()

    app.exec_()
    
    
def start():
    user_text = """\
█▀▄ █▀█ █░█ █▀▀ ▄▄ █▀▀ █▀▀ █▄░█ █▀▀   █▀▄ █▀▀ █ █▀▄ █▄▄
█▄▀ █▀▄ █▄█ █▄█ ░░ █▄█ ██▄ █░▀█ ██▄   █▄▀ █▄█ █ █▄▀ █▄█
    """
    coloretti = random.choice(["blue", "green", "red", "yellow", "magenta", "cyan"])
    console.print(Panel(Align(user_text, style=coloretti, align="center")))





console = Console()
user_data = {}  

def handle_drugs(drug_input):
    drug_names = [name.strip() for name in drug_input.split(',')]
    user_data["drugs"] = drug_names
    user_data["state"] = "data_processed"

    os.system("clear")

    user_text = """\
    
        █▀▄ █▀█ █░█ █▀▀ ▄▄ █▀▀ █▀▀ █▄░█ █▀▀   █▀▄ █▀▀ █ █▀▄ █▄▄
        █▄▀ █▀▄ █▄█ █▄█ ░░ █▄█ ██▄ █░▀█ ██▄   █▄▀ █▄█ █ █▄▀ █▄█
    """
    console.print(Panel(Align(user_text, style="bold yellow", align="center")))

    url = f"https://dgidb.org/api/v2/interactions.json?drugs={','.join(drug_names)}"

    try:
        with Progress() as progress:
            task = progress.add_task("[cyan]🚑 Loading Gene...", total=4)
            for i in range(4):
                progress.update(task, advance=1)
                time.sleep(0.85)  

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            json_data = response.json()

        user_data["gene_interactions"] = process_data(json_data)

        
        for i, (gene_name, data) in enumerate(user_data["gene_interactions"].items(), start=1):
            gene_long_name = f"{data['details']['geneLongName']}"
            message = f"\n{i}. 🧬 Interactions for gene: {gene_name}\n\n📒 Full gene name is: {gene_long_name}\n"
            scores = []
            drugs = []

            for j, drug in enumerate(data["drugs"]):
                scores.append(data['scores'][j])
                drugs.append(drug)
                score_color = random.choice(["red", "green", "blue", "magenta", "yellow", "cyan"])
                details_color = random.choice(["red", "green", "blue", "magenta", "yellow", "cyan"])
                message += f"\n  {chr(0x1F48A + j)} Drug: {drug} 💊\n  {chr(0x1F4AF)} Score: {data['scores'][j]} ⭐️\n  {chr(0x1F4DD)} Details: {data['details']['interactionTypes']} 📝\n"
                console.print(Panel(message, style=f"bold {details_color}", title="Drug-Gene Interaction"))

        
        gene_number = console.input("\n🌗 Now choose the gene to open in the graph (enter the number 0 to skip): ")
        if gene_number.isdigit() and 0 < int(gene_number) <= len(user_data["gene_interactions"]):
            selected_gene = list(user_data["gene_interactions"].keys())[int(gene_number) - 1]

            
            selected_data = user_data["gene_interactions"][selected_gene]
            plot_gene_interactions(selected_gene, selected_data)

    except ConnectionError as e:
        handle_exception(e, "NoConnectionException")
    except Timeout as e:
        handle_exception(e, "ConnectionTimeoutException")
    except RequestException as e:
        handle_exception(e, "NoResponseException")
    except RequestException as e:
        handle_exception(e, "ThrottledRequestException")
    except RequestException as e:
        handle_exception(e, "CaptchaChallengeException")
    except RequestException as e:
        handle_exception(e, "ConversationLimitException")
    except RequestException as e:
        handle_exception(e, "CreateConversationException")
    except RequestException as e:
        handle_exception(e, "GetConversationsException")
    except Exception as e:
        handle_exception(e)


def plot_gene_interactions(selected_gene, selected_data):
    
    all_genes = list(user_data["gene_interactions"].keys())
    all_scores = [user_data["gene_interactions"][gene]["scores"] for gene in all_genes]

    plt.figure(figsize=(12, 8))
    colors = plt.cm.viridis.colors

    for i, gene in enumerate(all_genes):
        gene_scores = all_scores[i]
        plt.bar([gene], gene_scores, color=colors[i])

    plt.bar(selected_gene, selected_data["scores"], color='yellow')  # Barra rossa per il gene selezionato
    plt.xlabel('Genes')
    plt.ylabel('Interaction Score')
    plt.title(f'Interactions for all genes with respect to: {selected_gene}')
    plt.xticks(rotation=45, ha="right")
    plt.legend(["Geni"] + all_genes, loc="upper left", bbox_to_anchor=(1, 1))

    plt.show()


def process_data(json_data):
    gene_interactions = {}

    matched_terms = json_data.get("matchedTerms", [])
    for term in matched_terms:
        drug_name = term.get("drugName", "N/A")
        interactions = term.get("interactions", [])
        for interaction in interactions:
            interaction_id = interaction.get("interactionId", "N/A")
            interaction_types = ", ".join(interaction.get("interactionTypes", []))
            gene_name = interaction.get("geneName", "N/A")
            gene_long_name = interaction.get("geneLongName", "N/A")
            gene_entrez_id = interaction.get("geneEntrezId", "N/A")
            sources = ", ".join(interaction.get("sources", []))
            pmids = ", ".join(map(str, interaction.get("pmids", [])))
            score = interaction.get("score", "N/A")

            if gene_name not in gene_interactions:
                gene_interactions[gene_name] = {
                    "drugs": [drug_name],
                    "scores": [score],
                    "details": {
                        "interactionId": interaction_id,
                        "interactionTypes": interaction_types,
                        "geneLongName": gene_long_name,
                        "geneEntrezId": gene_entrez_id,
                        "sources": sources,
                        "pmids": pmids
                    }
                }
            else:
                gene_interactions[gene_name]["drugs"].append(drug_name)
                gene_interactions[gene_name]["scores"].append(score)

    return gene_interactions


def handle_exception(exception, error_type=None):
    error_message = f"❌ An error occurred: {exception}"

    if error_type:
        error_message += f"\nException Type: {error_type}"

    console.print(Panel.fit(error_message))


if __name__ == "__main__":
    asyncio.run(main())
