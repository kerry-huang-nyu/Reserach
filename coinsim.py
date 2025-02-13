import numpy as np

# Setup
n = 1000
coins = np.random.rand(n)
coins = coins.sort()

# @param    bias is the probability of heads
# @return   True = Heads, False = Tails
def flip_biased(bias: float) -> bool:
    return np.random.rand() < bias # < vs <= is arbitrary here

# Adaptive
first = np.random.randint(0, n)
flips = 1
if flip_biased(coins[first]):
    # Got heads, looking for tails
    for i, coin in enumerate(coins):
        if i == first: continue # Flipped this coin already
        flips += 1
        if not flip_biased(coin): break # If we get tails, we're done
else:
    # Got tails, looking for heads
    for i, coin in enumerate(coins[::-1]):
        if i == first: continue
        flips += 1
        if flip_biased(coin): break # If we get heads, we're done

print("adaptive:")
print("n:", n)
print("coins:", coins)
print("flips:", flips)
print("==========================")

# Round-Robin
flips = 1
first_res = flip_biased(coins[0]) # Start with coin 0; could be n, arbitrary choice
backwards = True # Flag for round-robin ordering
i, j = 1, n - 1 # Skip 0 since that was our first flip
while i <= j:
    flips += 1
    if backwards: # Highest to lowest prob of heads
        current_res = flip_biased(coins[j])
        j -= 1
    else: # Highest to lowest prob of tails
        current_res = flip_biased(coins[i])
        i += 1
    if first_res != current_res: break # Got the side we wanted
    backwards = not backwards # Flip the ordering 

print("non-adaptive:")
print("flips:", flips)
print("==========================")