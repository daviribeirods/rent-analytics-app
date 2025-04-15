from playwright.sync_api import sync_playwright, Page
from utils.functions import (
    save_unique_links,
    generate_urls,
    get_n_properties
)

def get_df_moveis_urls():
    """_summary_
    """
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        context = browser.new_context()
        main_page = context.new_page()
        
        urls = generate_urls()
        
        for url in urls:
            
            # First time access
            main_page.goto(url=url)
            total_properties = get_n_properties(page=main_page)
            step_sum = 30
            current_step = 0
            page = 2
            
            while (current_step < total_properties):
                # Page navigation
                current_step += step_sum
                
                # Get all cards url locator
                url_cards_selector = ".new-card"
                url_cards = main_page.locator(url_cards_selector).all()
                
                # Extract URLs from cards locator
                property_urls = []
                for url_card in url_cards:
                    href = url_card.get_attribute('href')
                    if href:
                        property_urls.append(href)
                
                # Save unique URLs to file
                save_unique_links(property_urls, "data/raw/df_imoveis_rent_urls.txt")
                
                temp_url = url + f'?pagina={page}'
                page += 1
                main_page.goto(url=temp_url)
                
        browser.close()

def run_df_moveis():
    """Scrapes property data from DF Moveis website"""

    # Get all property urls from DF Moveis website and save to file
    # get_df_moveis_urls() # Uncomment to generate url links

    with sync_playwright() as p:
        
        # Get all property urls from file
        with open('data/raw/df_imoveis_rent_urls.txt', 'r', encoding='utf-8') as f:
            property_urls = [line.strip() for line in f]

        # Create a new browser instance
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        main_page = context.new_page()
        
        for url in property_urls:
            # Access each url
            main_url_domain = 'https://www.dfimoveis.com.br'
            current_url = main_url_domain + url
            main_page.goto(url=current_url)

            # Extract data from each url
            # Street / name property
            street_selector = 'h1.mb-0.font-weight-600.fs-1-5'
            street_locator = main_page.locator(street_selector)
            property_street = street_locator.text_content()
            
            # Get rent price and area
            general_info_selector = 'h6.mb-0.text-normal'
            general_info_locator = main_page.locator(general_info_selector).all()
            
            # Get property area
            property_area = general_info_locator[0].text_content()
            
            # Get neighborhood
            property_neighbor = general_info_locator[2].text_content()
            
            # Get city
            property_city = general_info_locator[3].text_content()
            
            # Get number of bedrooms
            property_number_bedrooms = general_info_locator[4].text_content()
            
            # Get the residents association fee
            property_condominium_fee = general_info_locator[5].text_content()
            
            # Get the property description
            property_published_date = general_info_locator[6].text_content()
            
            # Get the property rent price
            property_rent_price = general_info_locator[7].text_content()
            
            # Get the IPTU fee
            property_iptu_fee = general_info_locator[16].text_content()

            # Get last update date
            property_last_update_date = general_info_locator[17].text_content()
            
            # Get property description
            property_description = main_page.locator('p.w-100.pb-3.mb-0.texto-descricao').text_content()
            
            print('Hi')