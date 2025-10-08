# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Arcturus": {
        "RA": "14h 15m 39.7s",
        "Dec": "+19° 10′ 56″",
        "Magnitude": -0.05,
        "Spectral Type": "K1.5III"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names(star_data):
    for star_name in star_data:
        print(star_name)

def print_star_name_and_type(star_data):
    for star_name, star_properties in star_data.items():
        spectral_type = star_properties["Spectral Type"]
        print(f"{star_name}: {spectral_type}")

def find_stars_by_magnitude(star_data, limit=0.1):
    for star_name, star_details in star_data.items():
        if star_details["Magnitude"] > limit:
            print(star_name)

def find_star_closest_to_dec(star_data, target_dec=20.0):

    closest_star_name = None
    smallest_diff = float('inf')

    for star_name, details in star_data.items():
        dec_str = details["Dec"]
        cleaned_str = dec_str.replace('−', '-').replace('°', ' ').replace('′', ' ').replace('″', '')
        parts = cleaned_str.split()
        
        deg = float(parts[0])
        minutes = float(parts[1])
        seconds = float(parts[2])

        if deg < 0:
            decimal_dec = deg - (minutes / 60) - (seconds / 3600)
        else:
            decimal_dec = deg + (minutes / 60) + (seconds / 3600)

        diff = abs(decimal_dec - target_dec)

        if diff < smallest_diff:
            smallest_diff = diff
            closest_star_name = star_name
        elif diff == smallest_diff:
            current_brightest_mag = star_data[closest_star_name]["Magnitude"]
            if details["Magnitude"] < current_brightest_mag:
                closest_star_name = star_name
    
    print(f"\nThe star closest to {target_dec}° declination is: {closest_star_name}")

print("My favorite constellation is Cygnus the Swan")