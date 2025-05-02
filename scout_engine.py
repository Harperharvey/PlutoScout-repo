from playwright.sync_api import sync_playwright
import time

def run_scout_script(script, account_limit=5, message="Hey!"):
    results = []

    with sync_playwright() as p:
        for i in range(account_limit):
            try:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                for action in script:
                    if action['action'] == 'goto':
                        page.goto(action['url'])
                    elif action['action'] == 'click':
                        page.click(action['selector'])
                    elif action['action'] == 'type':
                        page.keyboard.type(action['text'])
                    elif action['action'] == 'wait':
                        time.sleep(action['ms'] / 1000)

                results.append({"account": i + 1, "status": "✅ Done"})
                browser.close()

            except Exception as e:
                results.append({"account": i + 1, "status": f"❌ Failed: {str(e)}"})
                try:
                    browser.close()
                except:
                    pass

    return results
