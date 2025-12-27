"""Now I want to create a class"""

from abc import ABC, abstractmethod


class Engine(ABC):
    """Interface for general Engine."""

    def __init__(self, power: int, weight: int) -> None:
        self.power = power
        self.weight = weight

    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...


class DiselEngine(Engine):
    """Concrete class that describes disel engine."""

    def __init__(self, power: int, weight: int, disel_consumption: int) -> None:
        super().__init__(power, weight)
        self.disel_consumption = disel_consumption

    def start(self) -> None:
        print("Engine started.")

    def stop(self) -> None:
        print("Engine stopped.")


class BioDiselEngine(Engine):
    """Concrete class that describes engine that workse on biodisel."""

    def __init__(self, power: int, weight: int, biodisel_consumption: int) -> None:
        super().__init__(power, weight)
        self.biodisel_consumption = biodisel_consumption

    def start(self) -> None:
        print("Engine started.")

    def stop(self) -> None:
        print("Engine stopped.")
