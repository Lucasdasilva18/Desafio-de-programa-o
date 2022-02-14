stars=1
def desenhar_escada(n):
    global stars
    if n > 1:
        print(" " * (n-1) + "*"*stars)
        stars = stars + 1
        desenhar_escada(n-1)
    if n == 1:
        print("*"*stars)
value = int(input('digite o número de degraus\n'))
desenhar_escada(value)