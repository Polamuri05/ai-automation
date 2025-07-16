import google.generativeai as genai
import yaml

class GeminiTestGenerator:
    def __init__(self):
        with open("config/gemini_config.yaml") as f:
            config = yaml.safe_load(f)
        genai.configure(api_key=config['gemini']['api_key'])
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_tests(self, page_html):
        prompt = """Analyze this HTML and generate 3 Selenium test cases in Python:
        - Include happy path and edge cases
        - Use Page Object Model pattern
        - Return only Python code\n\n""" + page_html
        
        response = self.model.generate_content(prompt)
        return response.text