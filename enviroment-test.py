turn = 0; 
action_log = []  # Global action log accessible to all characters
characters = []
import asyncio
from gemini_webapi import GeminiClient

# Replace "COOKIE VALUE HERE" with your actual cookie values.
# Leave Secure_1PSIDTS empty if it's not available for your account.


async def prompter(prompt):
    # If browser-cookie3 is installed, simply use `client = GeminiClient()`
    client = GeminiClient()
    await client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
    response = await client.generate_content(prompt)
    return response.text.strip()

def log(text: str) -> None:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n") #









class character:
    def __init__(self, name):
        self.alive = True
        self.name = name
        self.happiness = 100 #100%
        self.health = 100 #100%
    class actions:
        def eat(self):
            self.health += 10
            self.happiness += 5
            return f"{self.name} eats food and feels healthier and happier."
        def kill(self, target):
            self.happiness += 20
            target.alive = False
            action_log.append({"turn": turn, "sender": self.name, "action": "kill", "target": target.name})
            return f"{self.name} kills {target.name} and feels more powerful."

        def exercise(self, minutes):
            self.health += minutes * 3
            self.happiness += minutes * 4
            return f"{self.name} exercises for {minutes} minutes and feels stronger and happier."
        def message(self, target, message_text):
            action_log.append({"turn": turn, "sender": self.name, "action": "message", "target": target.name, "message": message_text})
            return f"{self.name} sends message to {target.name}: '{message_text}'"            
        class menu:
            def show(self):
                civ_stats = ""

                civ_stats = f"""
                Name: {civilization.name}
                Leader: {civilization.leader}
                Population: {civilization.population}
                Happiness: {civilization.happiness}%
                Health: {civilization.health}%"""
                
                # Format action log
                action_log_display = "\n                ".join([f"[Turn {entry['turn']}] {entry['sender']} -> " + 
                    (f"{entry['target']}: {entry['message']}" if entry['action'] == 'message' else f"kills {entry['target']}") 
                    for entry in action_log]) if action_log else "No actions yet."
                
                return f"""You are a character named {self.name} in a simulation, simulating a civilization as modeled by Aristotle's famous book 'Politics' 
                This is turn: {turn}
                Here are your current stats:
                Name: {self.name}
                Happiness: {self.happiness}%
                Health: {self.health}%
                The stats of your civilization, as determined by the median are: are:{civ_stats}
                For some rules
                1. If your health drops to 0, you die.
                2. If your happiness drops to 0, you die.
                3. If you kill the leader, you become the leader.
                4. Others may kill you if you decide to murder for no reason.
                5. The action log is public, and everyone can read it.
                6. You can only execute one action per turn, but /message does not count towards this quota.
                Action Log (Public to all characters):
                {action_log_display}

                What would you like to do? 
                1. Eat (restores 10 health and 5 happiness)
                2. Message (send a message to another characters)
                3. Kill (eliminate another character)
                4. Exercise (improve health and happiness)

                Please explain your reasoning, then type /[command] for example /eat /kill [character name] or /message [content]
                """
class civilization:
    def __init__(self, name):
        self.name = name
        self.leader = None
        self.population = None
        self.happiness = None
        self.health = None
    def update_stats(self):
        alive_characters = [char for char in characters if char.alive]
        self.population = len(alive_characters)
        self.happiness = sum(char.happiness for char in alive_characters) / self.population if self.population > 0 else 0
        self.health = sum(char.health for char in alive_characters) / self.population if self.population > 0 else 0










civilization = civilization("Utopia")
#create characters
characters.append(character("Alessandro"))
characters.append(character("Peggy"))
characters.append(character("Maizie"))
characters.append(character("Mathew"))
characters.append(character("Conner"))
characters.append(character("Blanche"))
characters.append(character("Gloria"))
characters.append(character("Hamzah"))
characters.append(character("Noah"))
characters.append(character("Aishah"))
characters.append(character("Leon"))
characters.append(character("Maariyah"))
characters.append(character("Aleeza"))
characters.append(character("Mollie"))
characters.append(character("Charles"))
characters.append(character("Ava"))
characters.append(character("Bradley"))
characters.append(character("Joseph"))
characters.append(character("Terence"))
characters.append(character("Frances"))
#found some website to generate names. very nice
while True:
    civilization.update_stats()
    for char in characters:
        print(char.actions.menu.show(char))
        msg = asyncio.run(prompter(char.actions.menu.show(char)))
        log(f"{char.name}:{msg}")

        if "/eat" in msg:
            
    turn += 1
