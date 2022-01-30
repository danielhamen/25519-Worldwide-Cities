def GetRandomCity(Amount):
    """
    Returns a random City from "Cities.txt"

    args:
        Amount (int): The amount of Cities to return
    """

    import random

    Cities_ = open(r"Cities\Cities.txt", "r", encoding="utf-8")
    Cities = Cities_.readlines()
    Cities_.close()

    def GetCity():
        """
        Returns a random City utilizing the "random.choice()" function/method
        """

        City = random.choice(Cities)
        City = str(City).replace("\n", "")

        return City

    if int(Amount) == 1:
        return GetCity()

    else:
        CitiesList = []

        for i in range(0, Amount):
            City = GetCity()

            CitiesList.append(City)

    return CitiesList
