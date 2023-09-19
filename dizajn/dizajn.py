def pozicija_visina(current_hight, promena):
    if current_hight <= 500 or current_hight >= 540:
        promena *= -1
    current_hight += 1*promena
    return current_hight