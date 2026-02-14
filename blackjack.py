# ---- Entrypoint ----
def main() -> None:
    
    try:
        game.main_loop()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting game. Goodbye.")
        sys.exit(0)


if __name__ == "__main__":
    main()