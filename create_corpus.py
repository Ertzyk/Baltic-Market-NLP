import re
from datasets import load_dataset

def generate_corpus(target_words = 100000, output_file = "latvian_corpus.txt"):
    # Download Latvian Wikipedia dataset
    dataset = load_dataset("wikimedia/wikipedia", "20231101.lv", split = "train")

    word_count = 0
    
    with open(output_file, "w", encoding = "utf-8") as f:
        for article in dataset:
            raw_text = article['text']
            
            # Remove punctuation
            cleaned_text = re.sub(r'[^\w\s]', '', raw_text)
            
            # Remove digits and underscores
            cleaned_text = re.sub(r'[\d_]', '', cleaned_text)
            
            # Convert everything to lowercase
            cleaned_text = cleaned_text.lower()
            
            # Split by whitespace to get a list of actual words
            words = cleaned_text.split()
            
            if not words:
                continue

            f.write("\n".join(words) + "\n")
            word_count += len(words)
            
            if word_count >= target_words:
                break
                
    print(f"Extracted {word_count} words and saved to {output_file}.")

if __name__ == "__main__":
    generate_corpus(100000)