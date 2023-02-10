class playerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        return print('Run')


player1 = playerCharacter('Boss')

print(player1.name)
print(player1.run())

