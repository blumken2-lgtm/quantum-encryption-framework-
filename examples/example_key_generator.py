# Example script to demonstrate aperiodic key generation
from src.key_generation import create_aperiodic_key_sequence

def main():
    # Generate 10 keys
    keys = create_aperiodic_key_sequence(10)
    print("Generated Keys:")
    for key in keys:
        print(key)

if __name__ == "__main__":
    main()