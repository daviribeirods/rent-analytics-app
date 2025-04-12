import os
from playwright.sync_api import Page
from utils.consts import (
    DF_MOVEIS_MAIN_URL,
    DF_MOVEIS_CITIES,
    STATE,
    CONTRACT_TYPE,
    PROPERTY_TYPES
)

def save_unique_links(links: list, filename: str = "/data/property_links.txt") -> None:
    """
    Save unique links to a file and remove duplicates from existing links
    
    Args:
        links (list): List of new links to save
        filename (str): Name of the file to save links to. Defaults to "property_links.txt"
    """
    existing_links = set()
    
    # Read existing links if file exists
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            existing_links = set(line.strip() for line in f)
    
    # Add new links and remove duplicates
    all_links = existing_links.union(links)
    
    # Save all unique links back to file
    with open(filename, 'w', encoding='utf-8') as f:
        for link in sorted(all_links):
            f.write(f"{link}\n")
            
    print(f"Saved {len(all_links)} unique links to {filename}")
    
def generate_urls():
    
    list_of_links = []
    for property_type in PROPERTY_TYPES:
        for city in DF_MOVEIS_CITIES:
            for contract_type in CONTRACT_TYPE:              
                local_url = f'{DF_MOVEIS_MAIN_URL}/{contract_type}/{STATE}/{city}/{property_type}'
                list_of_links.append(local_url)
    return list_of_links

def get_n_properties(page: Page):
    """Get the total number of properties in a DF Imóveis search

    Args:
        page (Page): the current playwright page in DF Imóveis website.

    Returns:
        _type_: The total number of properties in a DF Imóveis website search.
    """
    try:
        selector = 'h1.titulo-pagina.center-text'
        locator = page.locator(selector)
        text_content = locator.text_content()    
        
        clean_text = text_content.lstrip()
        parts = clean_text.split(' ')
        
        if len(parts) < 2:
            return 0
        
        return int(parts[0])
        
    except Exception:
        return 0