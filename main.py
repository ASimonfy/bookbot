import sys
from stats import analyzeBookText

def main():
    print("Usage: python3 main.py <path_to_book>")
    if (len(sys.argv) == 1):
        sys.exit(1)
    analyzeBookText(sys.argv[1])
    
main()