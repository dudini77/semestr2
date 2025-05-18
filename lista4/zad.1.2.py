import argparse 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def model_rozwoju(Y, T, N, beta, sigma, gamma): #ta funkcja defniuje uklad rownan rozniczkowych
    S, E, I, R = Y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]
def main(): #parsowanie argumentow, 
    parser = argparse.ArgumentParser(description='symulacja_SEIR')
    parser.add_argument('-N', type=int, default=1111, help='calkowita populacja: ')
    parser.add_argument('-S0', type=int, default=1109, help='liczba podatnych na początku: ')
    parser.add_argument('-E0', type=int, default=101, help='liczba eksponowanych: ')
    parser.add_argument('-I0', type= int, default=2, help='zarazeni na poczatku: ' )
    parser.add_argument('-R0', type= int, default= 0, help='liczba wyzdrowiałych na początku: ')
    parser.add_argument('-beta', type= float, default= 1.29, help='wskaznik transmisji: ')
    parser.add_argument('-sigma', type= float, default= 0.19, help= 'wskaznik inkubacji: ')
    parser.add_argument('-gamma', type=float, default= 0.34, help='wspolczynnik wyzdrowien: ')
    parser.add_argument('-T', type=int, default=160, help='ilosc dni: ')
    args=parser.parse_args() #wpisywanie argumentow w losowej kolejnosci
    N=args.N 
    S0, E0, I0, R0 = args.S0, args.E0, args.I0, args.R0
    beta, sigma, gamma = args.beta, args.sigma, args.gamma
    T= np.linspace(0, args.T, args.T) #tworzenie wektora (symulacji) - uplyw czasu
    Y0= [S0, E0, I0, R0]
    Z= odeint(model_rozwoju, Y0, T, args=(N, beta, sigma, gamma)) #funckja rozwiazujaca rownania rozniczkowe
    S, E, I, R = Z.T #przypisanie parametrow do czasu
    plt.figure(figsize=(10, 6))
    plt.plot(T, S, label='S - Podatni')
    plt.plot(T, E, label='E - Eksponowani')
    plt.plot(T, I, label='I - Zakażeni')
    plt.plot(T, R, label='R - Odzyskani')
    plt.xlabel('Czas (dni)')
    plt.ylabel('Liczba osób')
    plt.title('Model SEIR (argumenty w stylu uniksowym)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()
#wnioski: jesli beta wieksza np 1.5 to Wzrost liczby osób zakażonych następuje szybciej i osiąga większy szczyt.
#jesli beta mniejsza np 0.3 to szczyt epidemi jest nizszy i bardij rozciagniety w czasie


