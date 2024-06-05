import json

class CrewAI:
    def __init__(self):
        self.tasks = {
            "order": self.process_order,
            "status": self.check_status,
            "faq": self.answer_faq
        }
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_base.json', 'r') as f:
            return json.load(f)

    def process_order(self, message):
        return "Order has been placed successfully."

    def check_status(self, message):
        return "Your order is being processed."

    def answer_faq(self, message):
        for item in self.knowledge_base['faqs']:
            if message.lower() in item['question'].lower():
                return item['answer']
        return "I'm not sure about that. Let me connect you with an agent."

    def handle_message(self, message):
        for task in self.tasks:
            if task in message:
                return self.tasks[task](message)
        return "How can I assist you today?"
