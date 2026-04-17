class CoffeeOrder:
    BASES = ["espresso", "americano", "latte", "cappuccino"]
    SIZES = ["small", "medium", "large"]
    MILKS = ["none", "whole", "skim", "oat", "soy"]

    BASE_PRICES = {"espresso": 200, "americano": 250, "latte": 300, "cappuccino": 320}
    SIZE_MULT = {"small": 1.0, "medium": 1.2, "large": 1.4}
    MILK_PRICES = {"none": 0, "whole": 30, "skim": 30, "oat": 60, "soy": 50}
    SYRUP_PRICE = 40
    ICE_SURCHARGE = 0.2

    def __init__(
        self,
        base: str,
        size: str,
        milk: str = "none",
        syrups: tuple[str, ...] = (),
        sugar: int = 0,
        iced: bool = False,
    ):
        if not base or base not in self.BASES:
            raise ValueError(f"base должен быть одним из {self.BASES}")
        if not size or size not in self.SIZES:
            raise ValueError(f"size должен быть одним из {self.SIZES}")
        if milk not in self.MILKS:
            raise ValueError(f"milk должен быть одним из {self.MILKS}")
        if len(syrups) > 4:
            raise ValueError("максимум 4 сиропа")
        if not (0 <= sugar <= 5):
            raise ValueError("sugar должен быть от 0 до 5")

        self.base = base
        self.size = size
        self.milk = milk
        self.syrups: tuple[str, ...] = tuple(syrups)
        self.sugar = sugar
        self.iced = iced

        self.price: float = self._calc_price()
        self.description: str = self._make_description()

    def _calc_price(self) -> float:
        total = self.BASE_PRICES[self.base] * self.SIZE_MULT[self.size]
        total += self.MILK_PRICES[self.milk]
        total += len(self.syrups) * self.SYRUP_PRICE
        if self.iced:
            total *= (1 + self.ICE_SURCHARGE)
        return round(total, 2)

    def _make_description(self) -> str:
        desc = f"{self.size} {self.base}"
        if self.milk != "none":
            desc += f" with {self.milk} milk"
        if self.syrups:
            desc += " + " + ", ".join(self.syrups)
        if self.iced:
            desc += " (iced)"
        if self.sugar > 0:
            desc += f" {self.sugar} tsp sugar"
        return desc

    def __str__(self) -> str:
        return f"{self.description} — {self.price} RUB"


# if __name__ == "__main__":
#     order = CoffeeOrder(
#         base="latte",
#         size="large",
#         milk="oat",
#         syrups=("vanilla", "caramel"),
#         sugar=2,
#         iced=True
#     )
if __name__ == "__main__":
    order = CoffeeOrder(
        base="americano",
        size="small",
        milk="soy",
        syrups=("vanilla", "caramel"),
        sugar=5,
        iced=True
    )
    print(order)
    print(f"Цена: {order.price} RUB")
