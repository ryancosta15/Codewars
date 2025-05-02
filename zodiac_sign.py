def get_zodiac_sign(day, month):
    S = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
    if month == 1 or month == 4:
        d = 20
    elif month == 2:
        d = 19
    elif month ==  3 or month == 5 or month == 6:
        d = 21
    elif month == 11:
        d = 22
    elif month == 12:
        return S[0] if day >= 22 else S[11]
    else:
        d = 23
    return S[month] if day>= d else S[month-1]
