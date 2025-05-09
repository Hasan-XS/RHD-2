# wikipedia.py

import wikipediaapi


def get_wikipedia_answer(command: str) -> str:
    """
    Fetches a summary from Wikipedia based on the given command.

    Args:
        command (str): The topic or question to search on Wikipedia.

    Returns:
        str: Summary text if found, otherwise a fallback message.
    """
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='RichardAssistant/1.0 (ha3an.majidii@gmail.com)'
    )

    print(f"[Wikipedia Search] Query: {command}")
    page = wiki.page(command)

    if page.exists():
        return page.summary

    print(f"[Wikipedia] Page not found for '{command}', trying alternatives...")

    # Try disambiguation page
    disambiguation_page = wiki.page(f"{command} (disambiguation)")
    if disambiguation_page.exists():
        return disambiguation_page.summary

    # Try searching only the last word
    simplified_query = command.split(" ")[-1]
    simplified_page = wiki.page(simplified_query)
    if simplified_page.exists():
        return simplified_page.summary

    return "Sorry, I couldn't find any information about that."
