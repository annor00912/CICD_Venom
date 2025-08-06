import argparse
from core.engine import Engine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True)
    parser.add_argument('--interactive', action='store_true')
    args = parser.parse_args()

    if args.interactive:
        from cicdvenom.tui.dashboard import run_dashboard
        run_dashboard(args.target)
    else:
        Engine().run(args.target)

if __name__ == '__main__':
    main()