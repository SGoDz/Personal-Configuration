class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__" :
    print bcolors.WARNING   + "Warning  : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.FAIL      + "Fail     : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.OKGREEN   + "OK Green : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.OKBLUE    + "OK Blue  : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.HEADER    + "Header   : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.UNDERLINE + "Undeline : No active frommets remain. Continue?" + bcolors.ENDC
    print bcolors.BOLD      + "Bold     : No active frommets remain. Continue?" + bcolors.ENDC
