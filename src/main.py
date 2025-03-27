from playwright.sync_api import sync_playwright
from time import sleep
from crawlers.df_moveis import run_df_moveis

def main():

    # Run df moveis crawler
    run_df_moveis()

if __name__=='__main__':
    main()