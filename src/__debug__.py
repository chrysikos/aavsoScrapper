from scrapper import aavsoScrapper

def main():
    program = aavsoScrapper()
    program.doTheFuckingJob(
        [
            "--auid=ASASSN-21cu",
            "--savepath=/home/chrysikos/Repos/aavsoScrapper/src/"
        ])



main()