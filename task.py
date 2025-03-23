import random

N = 97
TEXT = "MODE:\nType 1 for Manual number of heads input\nType 2 for Random Generated Heads number\nType 0 for predefined hardcoded number\n\n > "

def max_strength(n):
    """
    Calculates the maximum power of a dragon flock with n heads,
    if the optimal decomposition predominantly includes 3s.
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

def max_strength_dp(n):
    """
    Calculates the maximum power of a dragon flock with n heads,
    where every dragon can have from 1 to 7 heads.
    dp[i] stores the maximum obtainable product by
    decomposing number i into terms each not greater than 7.
    """
    # Initialize array dp, dp[0] = 1 (empty decomposition)
    dp = [0] * (n + 1)
    dp[0] = 1

    # Calculate dp[i] for i from 1 to n
    for i in range(1, n + 1):
        best = 0
        # If i <= 7 we can consider not to decompose number i
        # which corresponds to the power of a one dragon with i heads
        if i <= 7:
            best = i
        # Go through all the possible terms j from 1 to min(i, 7)
        for j in range(1, min(i, 7) + 1):
            candidate = dp[i - j] * j
            if candidate > best:
                best = candidate
        dp[i] = best
    return dp[n]

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
        print("Max flock power of", N, "heads:", max_strength_dp(N), "DYNAMIC PROGRAMMING")
    else:
        print("OUT OF BOUNDS N VALUE! 0 < N < 100")
