import argparse
class DataIngestion:
  pass
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file", required=True, help="accepts a data file as argument")
  parser.add_argument("--strategy", default="mean", help="How to fill blank rows")
  args = parser.parse_args()

if __name__ == "__main__":
  main()
