import hashlib
import itertools
import string

# Function to detect hash type based on input length
def detect_hash_type(hash_value):
    hash_lengths = {
        32: 'md5',
        40: 'sha1',
        64: 'sha256',
        128: 'sha512'
    }
    return hash_lengths.get(len(hash_value), 'unknown')

# Function to generate charset based on user input
def generate_charset(options):
    charset = ''
    if 'n' in options:
        charset += string.digits  # Numbers
    if 'a' in options:
        charset += string.ascii_letters  # Alphabets (uppercase + lowercase)
    if 's' in options:
        charset += string.punctuation  # Special characters
    return charset

# Brute force function to try all combinations
def brute_force(hash_value, charset, hash_type, max_length=5):
    # Debug: Print the selected character set
    print(f"Using charset: {charset}")

    # Iterate over all lengths up to max_length
    for length in range(1, max_length + 1):
        print(f"Trying password length: {length}")

        # Create all combinations of the given charset
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)  # Convert tuple to string

            # Hash the guess using the correct hash type
            hash_guess = hashlib.new(hash_type, guess.encode()).hexdigest()

            # Debug: Show the current guess and its hash
            print(f"Guess: {guess}, Hash: {hash_guess}")

            # Check if the guessed hash matches the input hash
            if hash_guess == hash_value:
                return guess  # Return the password if found

    return None

# Main function to interact with the user and initiate cracking
def main():
    hash_value = input("Enter the hash to crack: ").strip()
    options = input("Choose character set (e.g., -n, -a, -s, -na, -nas): ").replace('-', '')
    max_length = int(input("Enter the maximum password length: "))

    # Detect the hash type
    hash_type = detect_hash_type(hash_value)
    if hash_type == 'unknown':
        print("Unknown hash type. Please try again.")
        return

    # Generate the character set based on input options
    charset = generate_charset(options)
    if not charset:
        print("No valid character set selected.")
        return

    print(f"Attempting to crack {hash_type} hash...")

    # Start brute-forcing
    result = brute_force(hash_value, charset, hash_type, max_length)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
