import random
import string
import time

def generate_random_word():
    """Generate a random word"""
    words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it',
             'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this',
             'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or',
             'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
             'code', 'program', 'data', 'file', 'system', 'user', 'time', 'way']
    return random.choice(words)

def create_file_with_rust(filename='hello.txt', size_mb=10):
    """
    Create a text file with 'rust' appearing exactly 3 times at random positions
    
    Args:
        filename: Name of the output file
        size_mb: Target size in MEGABYTES (default: 10MB - safe for testing)
    """
    target_size = size_mb * 1024 * 1024  # Convert MB to bytes
    
    # Calculate 3 random positions for "rust"
    rust_positions = sorted(random.sample(range(100, target_size - 100), 3))
    
    print(f"Creating {size_mb}MB file: {filename}")
    print(f"'rust' will appear at approximately byte positions: {rust_positions}")
    print("Writing file... (this may take a moment)")
    
    with open(filename, 'w', encoding='utf-8', buffering=8192*1024) as f:
        bytes_written = 0
        rust_index = 0
        word_count = 0
        
        while bytes_written < target_size:
            # Check if we need to insert "rust"
            if rust_index < 3 and bytes_written >= rust_positions[rust_index]:
                f.write('rust ')
                bytes_written += 5
                rust_index += 1
            else:
                # Write random word
                word = generate_random_word()
                f.write(word + ' ')
                bytes_written += len(word) + 1
                word_count += 1
                
                # Add newline every ~15 words
                if word_count % 15 == 0:
                    f.write('\n')
                    bytes_written += 1
            
            # Progress update every 1MB
            if bytes_written % (1024 * 1024) == 0:
                progress = (bytes_written / target_size) * 100
                print(f"Progress: {progress:.1f}% ({bytes_written / (1024*1024):.1f} MB)", end='\r')
    
    actual_size = bytes_written / (1024 * 1024)
    print(f"\n✓ File created: {filename}")
    print(f"✓ Size: {actual_size:.2f} MB")
    print(f"✓ 'rust' appears exactly 3 times")

if __name__ == "__main__":
    print("=" * 50)
    print("SAFE TEXT FILE GENERATOR")
    print("=" * 50)
    
    # CHOOSE YOUR SIZE (uncomment one):
    
    # For quick testing (1MB):
    #create_file_with_rust('hello.txt', size_mb=1)
    
    # For 10MB test:
    #create_file_with_rust('hello.txt', size_mb=10)
    
    # For 100MB:
    # create_file_with_rust('hello.txt', size_mb=100)
    
    # For 1GB (1024MB):
    create_file_with_rust('hello1gb.txt', size_mb=1024)
    
    # For 5GB (5120MB):
    # create_file_with_rust('hello.txt', size_mb=5120)
    
    print("\n✓ Done! Check 'hello.txt' in the same folder.")