class Animal:
    alive: list = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def reset_alive(cls) -> None:
        cls.alive.clear()

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.remove_dead()


def test_animal_constructor() -> None:
    Animal.reset_alive()
    lion = Animal("Lion King")

    assert hasattr(lion, "name"), \
        "Animal instance should have attribute 'name'"
    assert hasattr(lion, "health"), \
        "Animal instance should have attribute 'health'"
    assert hasattr(lion, "hidden"), \
        "Animal instance should have attribute 'hidden'"
    assert lion.name == "Lion King", \
        "'lion.name' should equal to 'Lion King'"
    assert lion.health == 100, \
        "'lion.health' should equal to 100'"
    assert lion.hidden is False, "'lion.hidden' should equal to False'"

    print("Current alive animals:", Animal.alive)

    assert len(Animal.alive) == 1, \
        "Constructor should add created animal to 'Animal.alive'"


if __name__ == "__main__":
    Animal.reset_alive()
    lion = Carnivore("Simba")
