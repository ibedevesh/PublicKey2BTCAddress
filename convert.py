import hashlib
from bitcoin import *

def public_key_to_address(public_key_hex):
    # Remove '04' prefix if present
    if public_key_hex.startswith('04'):
        public_key_hex = public_key_hex[2:]
    
    # Convert hex string to bytes
    public_key_bytes = bytes.fromhex(public_key_hex)
    
    # Perform SHA-256 hashing on the public key
    sha256_bpk = hashlib.sha256(public_key_bytes).digest()
    
    # Perform RIPEMD-160 hashing on the result of SHA-256
    ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
    
    # Convert back to hex string
    ripemd160_bpk_hex = ripemd160_bpk.hex()
    
    # Use bitcoin library to generate address
    address = pubkey_to_address('04' + public_key_hex)
    
    return address

def main():
    while True:
        public_key = input("Enter the Bitcoin public key (or 'q' to quit): ").strip()
        
        if public_key.lower() == 'q':
            break
        
        print(f"Debug: Input length: {len(public_key)}")
        print(f"Debug: Input: {public_key}")
        
        address = public_key_to_address(public_key)
        print(f"Bitcoin Address: {address}")
        print()

if __name__ == "__main__":
    main()
