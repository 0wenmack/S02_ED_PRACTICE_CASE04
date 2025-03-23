import random

N = 97
TEXT = "MODE:\nType 1 for Manual number of heads input\nType 2 for Random Generated Heads number\nType 0 for predefined hardcoded number\n\n > "

def max_strength(n):
    """
    Calculates the maximum power of a dragon flock with n heads,
    if optimal decomposition predominantly includes 3s.
    In case of n <= 3 returns n since theres no gains.
    """
    if n <= 3:
        return n
    # Divide n by 3: q – quantity of 3s, r – residue
    q, r = divmod(n, 3)
    if r == 0:
        return 3 ** q
    elif r == 1:
        # If residue = 1 its more beneficial to replace 3 with 4 (3+1)
        return (3 ** (q - 1)) * 4
    else:  # r == 2
        return (3 ** q) * 2

def generate_number(lower_bound=0, upper_bound=99):
    return random.randint(lower_bound, upper_bound)

if __name__ == "__main__":
    choice = int(input(TEXT))
    if (choice == 1):
        N = int(input("Enter a natural number between 0 and 100: "))
    elif (choice == 2):
        N = generate_number()
        print("Generated Number:", N)
    elif (choice == 0):
        pass
    else:
        print("Not a valid option")
        
    if (N<100 and N>0):
        print("Max flock power of", N, "heads:", max_strength(N))
    else:
        print("OUT OF BOUNDS N VALUE! 0 < N < 100")
