class Pokemon ():
    def __init__(self, name, detail_url):
        self.name = name
        self.detail_url = detail_url


    def info(self):
        return f"{self.name} ({self.detail_url})"
    
class FirePokemon(Pokemon):
    def __init__(self, name, detail_url):
        super().__init__(name, detail_url)

class GroundPokemon(Pokemon):
    def __init__(self, name, detail_url):
        super().__init__(name, detail_url)

class BugPokemon(Pokemon):
    def __init__(self, name, detail_url):
        super().__init__(name, detail_url)
