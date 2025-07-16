from src.ai_engine.gemini_analyzer import GeminiTestGenerator
from selenium import webdriver
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    # Fetch page HTML
    driver = webdriver.Chrome()
    driver.get(args.url)
    html = driver.page_source
    driver.quit()

    # Generate tests
    generator = GeminiTestGenerator()
    test_code = generator.generate_tests(html)
    
    with open("tests/generated/test_suite.py", "w") as f:
        f.write(test_code)

if __name__ == "__main__":
    main()