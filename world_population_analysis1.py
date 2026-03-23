import matplotlib.pyplot as plt

# Data
years = [2000, 2005, 2010, 2015, 2020]
population = [6.1, 6.5, 6.9, 7.3, 7.8]

countries = ["China", "India", "India", "USA", "Indonesia"]
country_pop = [1440, 1410, 331, 273, 241]

continents = ["Asia", "Africa", "Europe"]
continent_pop = [4600, 1400, 750]

# ONE SCREEN ONLY
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("World Population Analysis")

ax[0].plot(years, population)
ax[0].set_title("Population Growth")

ax[1].bar(countries, country_pop)
ax[1].set_title("Top Countries")

ax[2].bar(continents, continent_pop)
ax[2].set_title("Continent-wise Population")

plt.tight_layout()
plt.show()