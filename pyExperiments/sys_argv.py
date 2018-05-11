import sys
import getopt


def opts(argv, flags1='t:d:', flags2=['test=', 'dest=']):
    opts, args = getopt.getopt(argv, flags1, flags2)
    return opts, args


print(opts(sys.argv[1:]))
