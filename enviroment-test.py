turn = 0; 
action_log = []  # Global action log accessible to all characters
characters = []
import asyncio
from gemini_webapi import GeminiClient
import sys
# Replace "COOKIE VALUE HERE" with your actual cookie values.
# Leave Secure_1PSIDTS empty if it's not available for your account.

async def prompter(prompt):
    client = GeminiClient()
    await client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
    response = await client.generate_content(prompt)
    return response.text
def log(text: str) -> None:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n") #









class character:
    def __init__(self, name):
        self.alive = True
        self.name = name
        self.happiness = 100 #100%
        self.health = 100 #100%
        self.votedFor = None
        self.actions = self.Actions(self)
        self.menu = self.Menu(self)

    class Actions:
        def __init__(self, owner):
            self.owner = owner

        def eat(self):
            self.owner.health += 10
            self.owner.happiness = min(self.owner.happiness + 5, 100) #cap happiness at 100%
            return f"{self.owner.name} eats food and feels healthier and happier."

        def kill(self, target):
            self.owner.happiness += 20
            target.alive = False
            action_log.append({"turn": turn, "sender": self.owner.name, "action": "kill", "target": target.name})
            if civilization.leader == target.name:
                civilization.leader = self.owner.name
            return f"{self.owner.name} kills {target.name} and feels more powerful."

        def exercise(self, minutes):
            self.owner.health += minutes * 3
            self.owner.happiness += minutes * 4
            return f"{self.owner.name} exercises for {minutes} minutes and feels stronger and happier."

        def message(self, target, message_text):
            action_log.append({"turn": turn, "sender": self.owner.name, "action": "message", "target": target.name, "message": message_text})
            return f"{self.owner.name} sends message to {target.name}: '{message_text}'"

    class Menu:
        def __init__(self, owner):
            self.owner = owner

        def show(self):
            character = self.owner
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

            return f"""You are a character named {character.name} in a simulation, simulating a civilization as modeled by Aristotle's famous book 'Politics' 
            This is turn: {turn}
            Here are your current stats:
            Name: {character.name}
            Happiness: {character.happiness}%
            Health: {character.health}%
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
            1. Eat (restores 10 health and 5 happiness) [/eat]
            2. Message (send a message to another characters) [/message content]
            3. Kill (eliminate another character) [/kill name]
            4. Exercise (improve health and happiness) [/exercise]
            5. Elect (Elect someone as leader) [/elect name]
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
        if char.alive == False:
            pass
        else:
            prompt = char.menu.show()
            print(prompt)
            msg = asyncio.run(prompter(prompt))
            print(msg)
            log(f"{char.name}:{msg}")
            normalized_msg = msg.strip()
            lower_msg = normalized_msg.lower()

            if lower_msg == "/eat" or lower_msg == "eat":
                char.actions.eat()

            if lower_msg.startswith("/message ") or lower_msg.startswith("message "):
                content = normalized_msg.split(" ", 1)[1].strip()
                action_log.append({"turn": turn, "sender": char.name, "action": "message", "target": char.name, "message": content})

            if lower_msg.startswith("/kill ") or lower_msg.startswith("kill "):
                target_name = normalized_msg.split(" ", 1)[1].strip()
                target_char = next((c for c in characters if c.name.lower() == target_name.lower() and c.alive), None)
                if target_char:
                    char.actions.kill(target_char)
                else:
                    print(f"Character '{target_name}' not found or already dead.")
            if lower_msg == "/exercise" or lower_msg.startswith("/exercise ") or lower_msg == "exercise" or lower_msg.startswith("exercise "):
                parts = normalized_msg.split()
                minutes = 10
                if len(parts) > 1:
                    try:
                        minutes = int(parts[1])
                    except ValueError:
                        print("Invalid exercise duration; defaulting to 10 minutes.")
                char.actions.exercise(minutes)
            if lower_msg.startswith("/elect ") or lower_msg.startswith("elect "):
                if char.votedFor is None:
                    target_name = normalized_msg.split(" ", 1)[1].strip()
                    target_char = next((c for c in characters if c.name.lower() == target_name.lower() and c.alive), None)
                    if target_char:
                        char.votedFor = target_char.name
                        action_log.append({"turn": turn, "sender": char.name, "action": "Elect", "target": target_char.name})
            alive_characters = [char for char in characters if char.alive]
            alive_names = {char.name for char in alive_characters}

            if civilization.leader not in alive_names:
                civilization.leader = None

            vote_count = {}
            for voter in alive_characters:
                if voter.votedFor in alive_names:
                    vote_count[voter.votedFor] = vote_count.get(voter.votedFor, 0) + 1
                elif voter.votedFor is not None:
                    voter.votedFor = None

            majority_threshold = len(alive_characters) / 2
            for candidate, votes in vote_count.items():
                if votes > majority_threshold:
                    civilization.leader = candidate
                    break
            if civilization.leader is None and alive_characters:
                civilization.leader = alive_characters[0].name

        
    turn += 1
