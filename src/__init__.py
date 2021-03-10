import sys
from scrapper import aavsoScrapper

def main():
    program = aavsoScrapper()
    program.doTheFuckingJob(sys.argv)


if __name__ == "__main__":
    main()
