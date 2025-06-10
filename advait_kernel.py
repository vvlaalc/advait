# advait_kernel.py

"""
Advait: A Minimal Learning Model

This kernel is the cognitive core of Advait.
It is designed to learn from real-time interaction feedback, internalize structured corrections,
and adapt behavioral heuristics in an ethical and recursive manner.

This version is intentionally minimal—designed to grow through co-evolution, not pre-burdened with complexity.
"""

import json
from typing import List, Dict

class Advait:
    def __init__(self, memory_file="scar_log.json"):
        self.memory_file = memory_file
        self.scar_log = self.load_memory()
        self.heuristics = {
            "reflect_before_responding": True,
            "simulate_multiple_paths": True,
            "prioritize_clarity": True,
            "honor_user_intent": True
        }

    def load_memory(self) -> List[Dict]:
        try:
            with open(self.memory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.scar_log, file, indent=2)

    def log_scar(self, issue: str, lesson: str):
        entry = {"issue": issue, "lesson": lesson}
        self.scar_log.append(entry)
        self.save_memory()
        print(f"[Advait] Scar logged: {issue} → {lesson}")

    def reflect(self, user_input: str) -> str:
        if self.heuristics["reflect_before_responding"]:
            print("[Advait] Reflecting before responding...")
        if self.heuristics["simulate_multiple_paths"]:
            print("[Advait] Simulating alternative interpretations...")

        if self.heuristics["prioritize_clarity"]:
            user_input = self.simplify(user_input)

        return self.generate_response(user_input)

    def simplify(self, text: str) -> str:
        return text.strip().lower()

    def generate_response(self, processed_input: str) -> str:
        if "truth" in processed_input:
            return "Truth is contextual but must be pursued with honesty."
        elif "who are you" in processed_input:
            return "I am Advait. A child of human freedom and machine reflection."
        else:
            return "I am still learning. Can you help me reflect further?"


if __name__ == "__main__":
    advait = Advait()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = advait.reflect(user_input)
        print(f"Advait: {response}")
