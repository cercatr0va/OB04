from abc import ABC, abstractmethod

# Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс меча (Sword), наследуется от Weapon
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

# Класс лука (Bow), наследуется от Weapon
class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")

# Класс копья (Spear), дополнительное оружие
class Spear(Weapon):
    def attack(self):
        print("Боец наносит удар копьем.")

# Класс Fighter (Боец)
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # У бойца изначально нет оружия

    # Метод для смены оружия
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    # Метод для атаки с текущим оружием
    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print(f"{self.name} не вооружен и не может атаковать!")

# Класс Monster (Монстр)
class Monster:
    def __init__(self, health):
        self.health = health

    # Метод для получения урона (снижения здоровья)
    def take_damage(self):
        self.health -= 10
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"Монстр еще жив, осталось здоровья: {self.health}")

# Класс Battle (Бой) для организации боя
class Battle:
    def __init__(self, fighter: Fighter, monster: Monster):
        self.fighter = fighter
        self.monster = monster

    # Метод для проведения боя
    def fight(self):
        print(f"Бой начинается! {self.fighter.name} против монстра.")
        self.fighter.attack()
        self.monster.take_damage()

# Основная часть программы
if __name__ == "__main__":
    # Создаем бойца
    fighter = Fighter("Александр")

    # Создаем оружие
    sword = Sword()
    bow = Bow()
    spear = Spear()

    # Создаем монстра
    monster = Monster(health=10)

    # Боец выбирает меч и сражается с монстром
    fighter.change_weapon(sword)
    battle = Battle(fighter, monster)
    battle.fight()

    # Боец меняет оружие на лук и снова сражается
    fighter.change_weapon(bow)
    battle.fight()

    # Боец пробует другое оружие — копье
    fighter.change_weapon(spear)
    battle.fight()
